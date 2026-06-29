# MANUAL TÉCNICO Y GUÍA DE USO
## Biblioteca Virtual Leonardo Infante (Edición Nube)

Este documento explica el funcionamiento completo de la plataforma, actualizada para su despliegue en **Vercel** con persistencia en **MongoDB Atlas**.

### 1. OBJETIVO DEL PROYECTO
Proporcionar una plataforma educativa digital escalable y de alta disponibilidad para el acceso a recursos académicos, eliminando la dependencia de almacenamiento local y garantizando la persistencia de las sugerencias de los usuarios.

### 2. TECNOLOGÍAS UTILIZADAS
*   **Backend:** Python 3.13 / Flask.
*   **Base de Datos:** MongoDB Atlas (NoSQL).
*   **Despliegue:** Vercel (Serverless Functions).
*   **Frontend:** HTML5, CSS3, JavaScript Vanilla.
*   **Variables de Entorno:** Python-dotenv.

### 3. ESTRUCTURA DEL PROYECTO
```text
biblioteca-virtual/
├── app.py              # Lógica principal y conexión a DB
├── vercel.json         # Configuración de despliegue en Vercel
├── GUIA_DESPLIEGUE.md  # Instrucciones paso a paso para la nube
├── requirements.txt    # Dependencias del sistema
├── libros.json         # Datos semilla (Seed data)
├── static/             # Archivos estáticos (CSS, JS, Imágenes)
└── templates/          # Plantillas HTML
```

### 4. FUNCIONAMIENTO DEL SISTEMA
1.  **Arranque:** El sistema verifica la existencia de `MONGO_URI`.
2.  **Persistencia:** Las sugerencias ya no se pierden al reiniciar el servidor, se guardan en la nube.
3.  **Carga Dinámica:** Los libros se sirven desde MongoDB; si la base de datos está vacía, se sincroniza automáticamente con el archivo JSON local.

### 5. SISTEMA DE SUGERENCIAS
El formulario envía una petición POST a `/sugerir`. El backend procesa el objeto y lo inserta en la colección `sugerencias`. En el panel de MongoDB Atlas se pueden consultar estas peticiones en tiempo real.

### 6. EJECUCIÓN Y DESPLIEGUE
Para ejecutar localmente con persistencia:
1. Crear un archivo `.env`.
2. Añadir `MONGO_URI=tu_cadena_de_conexion`.
3. Ejecutar `python app.py`.

Para desplegar:
1. Sincronizar con GitHub.
2. Importar en Vercel.
3. Configurar la Environment Variable `MONGO_URI`.

### 7. POSIBLES MEJORAS IMPLEMENTADAS
*   ✅ **Hosting online:** Implementado mediante Vercel.
*   ✅ **Base de Datos:** Migrado de JSON a MongoDB.
*   ✅ **Escalabilidad:** Arquitectura preparada para miles de usuarios.
