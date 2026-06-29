# DIAGRAMAS DEL SISTEMA - BIBLIOTECA VIRTUAL

## 1. Diagrama de Entidad-Relación (Base de Datos NoSQL)

Aunque utilizamos MongoDB (orientado a documentos), este es el modelo lógico de los datos:

```mermaid
erDiagram
    LIBRO {
        string titulo "Título del libro"
        string materia "Categoría académica"
        string anio "Año escolar (1ro - 5to)"
        string imagen "Ruta o URL de la portada"
        string link "Enlace de descarga/lectura"
    }
    SUGERENCIA {
        string nombre "Nombre del solicitante"
        string libro "Título sugerido"
        string comentario "Razón de la sugerencia"
    }
```

## 2. Flujo de Consulta de Libros (Ruta Principal)

Este flujo describe cómo el sistema decide de dónde obtener la información al cargar la página.

```mermaid
graph TD
    A[Inicio: Navegador carga /] --> B{¿Variable MONGO_URI configurada?}
    B -- Sí --> C[Conectar a MongoDB Atlas]
    C --> D{¿Colección 'libros' tiene datos?}
    D -- No --> E[Leer 'libros.json' local]
    E --> F[Cargar datos en MongoDB]
    F --> G[Obtener libros de DB]
    D -- Sí --> G
    B -- No --> H[Leer 'libros.json' local]
    G --> I[Renderizar 'index.html' con la lista]
    H --> I
    I --> J[Fin]
```

## 3. Flujo de Sugerencias (Persistencia)

Describe el proceso desde que el usuario envía el formulario hasta que se guarda permanentemente.

```mermaid
graph TD
    A[Inicio: Usuario envía sugerencia] --> B[Recibir JSON en /sugerir]
    B --> C{¿Conexión a MongoDB activa?}
    C -- Sí --> D[Insertar documento en 'sugerencias']
    C -- No --> E[Añadir al archivo 'sugerencias.json' local]
    D --> F[Enviar respuesta de éxito]
    E --> F
    F --> G[Fin]
```
