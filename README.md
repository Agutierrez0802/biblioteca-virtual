# 📚 Biblioteca Virtual Leonardo Infante

Biblioteca digital escolar para el acceso a libros de texto en formato PDF, desarrollada como proyecto de servicio comunitario para el Complejo Educativo Leonardo Infante, Campo Rico, Petare, Caracas.

## 🎯 Descripción

Esta aplicación web permite a los estudiantes de 1° a 5° año de secundaria acceder a un catálogo de libros de texto organizados por materia y año escolar. Los libros están alojados en Google Drive y pueden consultarse en línea.

### Funcionalidades
- 📖 Catálogo de ~36 libros de texto
- 🔍 Búsqueda por título
- 🏷️ Filtros por materia y año escolar
- 💡 Formulario de sugerencias de libros
- 🌙 Modo oscuro
- 📱 Diseño responsivo
- 🕐 Reloj en tiempo real

## 🛠️ Stack Tecnológico

| Componente | Tecnología |
|-----------|------------|
| Backend | Python 3.13 + Flask 3.1 |
| Base de Datos | MongoDB Atlas (con fallback JSON) |
| Frontend | HTML5, CSS3, JavaScript |
| Deploy | Vercel (Serverless) |

## 🚀 Instalación Local

### Prerrequisitos
- Python 3.10+
- pip

### Pasos

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/TU_USUARIO/Biblioteca_Virtual.git
   cd Biblioteca_Virtual
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   ```bash
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar variables de entorno**
   ```bash
   cp .env.example .env
   # Editar .env con tu URI de MongoDB Atlas
   ```

6. **Ejecutar**
   ```bash
   python app.py
   ```
   La aplicación estará disponible en `http://localhost:5000`

## ☁️ Despliegue en Vercel

Consulta la [Guía de Despliegue](GUIA_DESPLIEGUE.md) para instrucciones detalladas sobre:
- Configuración de MongoDB Atlas
- Despliegue en Vercel via GitHub

## 📁 Estructura del Proyecto

```
├── app.py              # Servidor Flask
├── vercel.json         # Configuración Vercel
├── requirements.txt    # Dependencias Python
├── libros.json         # Datos de libros
├── sugerencias.json    # Sugerencias almacenadas (fallback local)
├── templates/
│   └── index.html      # Plantilla principal
├── static/
│   ├── css/style.css   # Estilos
│   ├── js/script.js    # Lógica del cliente
│   └── img/            # Imágenes y portadas
└── docs/               # Documentación técnica
```

## 👥 Autores

Proyecto de Servicio Comunitario — IUPSM (Instituto Universitario Politécnico Santiago Mariño), 2026.

## 📄 Licencia

Proyecto académico de servicio comunitario.
