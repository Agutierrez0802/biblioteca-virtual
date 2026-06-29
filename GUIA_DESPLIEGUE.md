# Despliegue en Vercel con Persistencia (MongoDB)

Para que este proyecto funcione en Vercel y los datos no se borren, hemos migrado de archivos JSON locales a una base de datos en la nube (**MongoDB Atlas**).

## Pasos para la Implementación

### 1. Configurar MongoDB Atlas (Gratis)
1. Crea una cuenta en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Crea un Cluster gratuito (M0).
3. En **Database Access**, crea un usuario y contraseña.
4. En **Network Access**, permite el acceso desde cualquier IP (`0.0.0.0/0`) para que Vercel pueda conectarse.
5. Ve a **Clusters** > **Connect** > **Connect your application** y copia la cadena de conexión (URI). Debería verse así:
   `mongodb+srv://<usuario>:<password>@cluster0.xxxxx.mongodb.net/?retryWrites=true&w=majority`

### 2. Preparar el Repositorio en GitHub
1. Sube este proyecto a un repositorio de GitHub.
2. Asegúrate de incluir los archivos: `app.py`, `requirements.txt`, `vercel.json`, `static/` y `templates/`.

### 3. Desplegar en Vercel
1. Ve a [Vercel](https://vercel.com/) y conecta tu cuenta de GitHub.
2. Selecciona el repositorio de la Biblioteca.
3. **IMPORTANTE:** En la sección **Environment Variables**, añade una nueva variable:
   - **Key:** `MONGO_URI`
   - **Value:** (La cadena de conexión que copiaste de MongoDB Atlas).
4. Haz clic en **Deploy**.

## Cambios Realizados en el Proyecto
- **`vercel.json`**: Configuración para que Vercel reconozca la aplicación Flask.
- **`app.py`**: Ahora intenta conectarse a MongoDB. Si no hay conexión, usa los archivos JSON como respaldo (solo lectura en Vercel).
- **`requirements.txt`**: Se añadieron `pymongo` y `python-dotenv`.

## Persistencia
- Las sugerencias ahora se guardan en la colección `sugerencias` de MongoDB.
- La primera vez que abras la app, los libros de `libros.json` se cargarán automáticamente en la base de datos.
