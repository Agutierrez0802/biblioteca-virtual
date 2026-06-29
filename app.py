from flask import Flask, render_template, request, jsonify
import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuración de MongoDB
# En desarrollo usará una variable local, en Vercel se configurará en el panel
MONGO_URI = os.getenv('MONGO_URI')

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client['biblioteca_db']
    libros_col = db['libros']
    sugerencias_col = db['sugerencias']
else:
    print("ADVERTENCIA: No se encontró MONGO_URI. Usando archivos JSON locales (No persistente en Vercel).")

@app.route('/')
def index():
    if MONGO_URI:
        libros = list(libros_col.find({}, {'_id': False}))
        # Si la base de datos está vacía, cargar desde el JSON inicial
        if not libros:
            with open('libros.json', 'r', encoding='utf-8') as file:
                libros = json.load(file)
                libros_col.insert_many(libros)
    else:
        with open('libros.json', 'r', encoding='utf-8') as file:
            libros = json.load(file)

    return render_template('index.html', libros=libros)


@app.route('/sugerir', methods=['POST'])
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
