from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

load_dotenv()

app = Flask(__name__)
# Secret key para firmar las cookies de la sesión
app.secret_key = os.getenv('SECRET_KEY', 'clave-secreta-por-defecto-123')

MONGO_URI = os.getenv('MONGO_URI')

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client['biblioteca_db']
    libros_col = db['libros']
    sugerencias_col = db['sugerencias']
    usuarios_col = db['usuarios']
    
    # Crear usuario admin por defecto si no existe ninguno
    if usuarios_col.count_documents({}) == 0:
        usuarios_col.insert_one({
            "correo": "admin@biblioteca.com",
            "password_hash": generate_password_hash("admin123")
        })
else:
    print("ADVERTENCIA: No se encontró MONGO_URI. Usando archivos JSON locales (No persistente en Vercel).")

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
                return redirect(url_for('index'))
        else:
            # Fallback local
            if correo == "admin@biblioteca.com" and password == "admin123":
                session['usuario'] = correo
                return redirect(url_for('index'))
                
        return render_template('login.html', error="Credenciales incorrectas")
        
    return render_template('login.html')

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

if __name__ == '__main__':
    app.run(debug=True)
