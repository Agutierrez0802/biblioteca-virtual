from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pymongo import MongoClient
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from itsdangerous import URLSafeTimedSerializer

load_dotenv()

app = Flask(__name__)
# Secret key para firmar las cookies de la sesión
app.secret_key = os.getenv('SECRET_KEY', 'clave-secreta-por-defecto-123')

# Serializador para generar tokens de recuperación
s = URLSafeTimedSerializer(app.secret_key)

MONGO_URI = os.getenv('MONGO_URI')

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client['biblioteca_db']
    libros_col = db['libros']
    sugerencias_col = db['sugerencias']
    usuarios_col = db['usuarios']
    config_col = db['configuracion']
    
    # Crear usuario admin por defecto si no existe ninguno
    if usuarios_col.count_documents({}) == 0:
        usuarios_col.insert_one({
            "correo": "admin@biblioteca.com",
            "password_hash": generate_password_hash("admin123"),
            "rol": "admin"
        })
else:
    print("ADVERTENCIA: No se encontró MONGO_URI. Usando archivos JSON locales (No persistente en Vercel).")

# Decorador para administradores
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session or session.get('rol') != 'admin':
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

# Decorador para proteger rutas
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'usuario' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        
        if MONGO_URI:
            user = usuarios_col.find_one({"correo": correo})
            if user and check_password_hash(user['password_hash'], password):
                session['usuario'] = correo
                session['rol'] = user.get('rol', 'estudiante')
                return redirect(url_for('index'))
        else:
            # Fallback local
            if correo == "admin@biblioteca.com" and password == "admin123":
                session['usuario'] = correo
                session['rol'] = "admin"
                return redirect(url_for('index'))
                
        return render_template('login.html', error="Credenciales incorrectas")
        
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        correo = request.form.get('correo')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')
        
        if password != confirm:
            return render_template('register.html', error="Las contraseñas no coinciden")
            
        if MONGO_URI:
            if usuarios_col.find_one({"correo": correo}):
                return render_template('register.html', error="El correo ya está registrado")
                
            usuarios_col.insert_one({
                "correo": correo,
                "password_hash": generate_password_hash(password),
                "rol": "estudiante"
            })
            # Iniciar sesión automáticamente
            session['usuario'] = correo
            session['rol'] = "estudiante"
            return redirect(url_for('index'))
            
    return render_template('register.html')

def send_reset_email(to_email, reset_url):
    config = config_col.find_one({"tipo": "correo"})
    if not config:
        print("ERROR: Configuración SMTP no establecida en la BD.")
        return False
        
    sender_email = config.get('email')
    sender_password = config.get('password')
    smtp_server = config.get('smtp_server', 'smtp.gmail.com')
    smtp_port = int(config.get('smtp_port', 587))
    
    msg = MIMEMultipart()
    msg['From'] = f"Biblioteca Virtual <{sender_email}>"
    msg['To'] = to_email
    msg['Subject'] = "Recuperación de Contraseña - Biblioteca Virtual"
    
    body = f"""
    Hola,
    
    Recibimos una solicitud para restablecer la contraseña de tu cuenta.
    Haz clic en el siguiente enlace para crear una nueva contraseña (es válido por 1 hora):
    
    {reset_url}
    
    Si no solicitaste este cambio, puedes ignorar este correo.
    """
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print("Error enviando correo:", e)
        return False

@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        correo = request.form.get('correo')
        if MONGO_URI:
            user = usuarios_col.find_one({"correo": correo})
            if user:
                # Generar token
                token = s.dumps(correo, salt='recover-key')
                reset_url = url_for('reset_password', token=token, _external=True)
                
                # Enviar correo
                enviado = send_reset_email(correo, reset_url)
                if enviado:
                    return render_template('recuperar.html', success="Se ha enviado un enlace de recuperación a tu correo.")
                else:
                    return render_template('recuperar.html', error="Hubo un problema enviando el correo. Revisa la configuración SMTP.")
            else:
                # Simulamos éxito para no revelar si un correo existe o no (seguridad)
                return render_template('recuperar.html', success="Si el correo existe, se enviará un enlace de recuperación.")
    return render_template('recuperar.html')

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        # El token expira en 3600 segundos (1 hora)
        correo = s.loads(token, salt='recover-key', max_age=3600)
    except Exception:
        return render_template('recuperar.html', error="El enlace de recuperación es inválido o ha expirado.")
        
    if request.method == 'POST':
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')
        
        if password != confirm:
            return render_template('reset_password.html', token=token, error="Las contraseñas no coinciden")
            
        if MONGO_URI:
            usuarios_col.update_one(
                {"correo": correo},
                {"$set": {"password_hash": generate_password_hash(password)}}
            )
            return redirect(url_for('login'))
            
    return render_template('reset_password.html', token=token)

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    if MONGO_URI:
        libros = list(libros_col.find({}, {'_id': False}))
        if not libros:
            with open('libros.json', 'r', encoding='utf-8') as file:
                libros = json.load(file)
                libros_col.insert_many(libros)
    else:
        with open('libros.json', 'r', encoding='utf-8') as file:
            libros = json.load(file)

    return render_template('index.html', libros=libros)

@app.route('/sugerir', methods=['POST'])
@login_required
def sugerir():
    data = request.json

    if MONGO_URI:
        sugerencias_col.insert_one(data)
    else:
        # Fallback local (no persistente en Vercel)
        if os.path.exists('sugerencias.json'):
            with open('sugerencias.json', 'r', encoding='utf-8') as file:
                sugerencias = json.load(file)
        else:
            sugerencias = []
        
        sugerencias.append(data)
        with open('sugerencias.json', 'w', encoding='utf-8') as file:
            json.dump(sugerencias, file, indent=4, ensure_ascii=False)

    return jsonify({
        "mensaje": "Sugerencia enviada correctamente"
    })

@app.route('/admin', methods=['GET'])
@admin_required
def admin_panel():
    if MONGO_URI:
        usuarios = list(usuarios_col.find({}, {'_id': False, 'password_hash': 0}))
        config = config_col.find_one({"tipo": "correo"}) or {}
    else:
        usuarios = [{"correo": "admin@biblioteca.com", "rol": "admin"}]
        config = {}
    return render_template('admin.html', usuarios=usuarios, config=config)

@app.route('/admin/config_correo', methods=['POST'])
@admin_required
def config_correo():
    if MONGO_URI:
        email = request.form.get('email')
        password = request.form.get('password')
        smtp_server = request.form.get('smtp_server', 'smtp.gmail.com')
        smtp_port = request.form.get('smtp_port', '587')
        
        config_col.update_one(
            {"tipo": "correo"},
            {"$set": {
                "email": email, 
                "password": password,
                "smtp_server": smtp_server,
                "smtp_port": smtp_port
            }},
            upsert=True
        )
    return redirect(url_for('admin_panel'))

@app.route('/admin/usuario', methods=['POST'])
@admin_required
def crear_usuario():
    if MONGO_URI:
        correo = request.form.get('correo')
        password = request.form.get('password')
        rol = request.form.get('rol', 'estudiante')
        if not usuarios_col.find_one({"correo": correo}):
            usuarios_col.insert_one({
                "correo": correo,
                "password_hash": generate_password_hash(password),
                "rol": rol
            })
    return redirect(url_for('admin_panel'))

@app.route('/admin/usuario/eliminar', methods=['POST'])
@admin_required
def eliminar_usuario():
    if MONGO_URI:
        correo = request.form.get('correo')
        if correo != session.get('usuario'):
            usuarios_col.delete_one({"correo": correo})
    return redirect(url_for('admin_panel'))

if __name__ == '__main__':
    app.run(debug=True)
