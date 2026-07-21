# 📚 Biblioteca Virtual Leonardo Infante

Biblioteca digital escolar desarrollada como proyecto de servicio comunitario para el **Complejo Educativo Leonardo Infante**, ubicado en Campo Rico, Petare, Caracas — Venezuela.

Su propósito es facilitar a los estudiantes de educación secundaria el acceso gratuito a sus libros de texto en formato digital (PDF), organizados por materia y año escolar, disponibles desde cualquier dispositivo con conexión a internet.

---

## 🎯 Objetivo del Proyecto

Brindar una herramienta tecnológica que permita a la comunidad estudiantil del Complejo Educativo Leonardo Infante consultar y descargar sus libros de texto de manera sencilla, eliminando la barrera del acceso físico al material bibliográfico.

Este proyecto nace como parte del requisito de **Servicio Comunitario** del Instituto Universitario Politécnico Santiago Mariño (IUPSM), con el fin de aportar una solución real a una necesidad de la comunidad educativa.

---

## ✨ Funcionalidades

- 📖 **Catálogo de libros** — Más de 35 libros de texto de la Colección Bicentenario, organizados por materia y año escolar (1° a 5° año).
- 🔍 **Búsqueda por título** — Barra de búsqueda para encontrar libros rápidamente por nombre.
- 🏷️ **Filtros por materia y año** — Filtrado dinámico por área de conocimiento y nivel académico.
- 💡 **Formulario de sugerencias** — Los usuarios pueden sugerir libros que desean que se agreguen al catálogo.
- 🌙 **Modo oscuro** — Alternancia entre tema claro y oscuro para una lectura cómoda.
- 📱 **Diseño responsivo** — Interfaz adaptable a computadoras, tabletas y teléfonos móviles.
- 🕐 **Reloj en tiempo real** — Visualización de la hora actual en la interfaz.

---

## 📚 Catálogo de Materias

El catálogo incluye libros de las siguientes áreas de conocimiento:

| Materia | Años disponibles |
|---------|-----------------|
| Ciencias Naturales | 1°, 2°, 3°, 4°, 5° |
| Ciencias Sociales | 1°, 2°, 3°, 4°, 5° |
| Matemática | 1°, 2°, 3°, 4°, 5° |
| Lengua y Literatura | 1°, 2°, 3°, 4°, 5° |
| Inglés | 1°, 2°, 3°, 4°, 5° |
| Artes (Educación Artística) | 1°, 2° |

Los libros están alojados en **Google Drive** y pueden consultarse directamente en línea desde el navegador.

---

## 🛠️ Tecnologías Utilizadas

| Componente | Tecnología |
|-----------|------------|
| Backend | Python 3.13 + Flask 3.1 |
| Frontend | HTML5, CSS3, JavaScript |
| Base de Datos | MongoDB Atlas (con respaldo en archivos JSON locales) |
| Motor de plantillas | Jinja2 |
| Despliegue | Vercel (Serverless Functions) |
| Control de versiones | Git + GitHub |

---

## 🚀 Instalación Local

### Prerrequisitos

- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git

### Pasos de instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Agutierrez0802/biblioteca-virtual.git
   cd biblioteca-virtual
   ```

2. **Crear un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar el entorno virtual**
   ```bash
   # Windows
   venv\Scripts\activate

   # Linux / macOS
   source venv/bin/activate
   ```

4. **Instalar las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar las variables de entorno**
   ```bash
   cp .env.example .env
   ```
   Editar el archivo `.env` con la URI de conexión a MongoDB Atlas. Si no se configura, la aplicación funcionará en modo local utilizando los archivos JSON incluidos.

6. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```
   La aplicación estará disponible en `http://localhost:5000`

---

## ☁️ Despliegue en Vercel

La aplicación está configurada para desplegarse en **Vercel** como una Serverless Function de Python. Para instrucciones detalladas sobre:

- Configuración de MongoDB Atlas en la nube
- Vinculación del repositorio de GitHub con Vercel
- Configuración de variables de entorno en el panel de Vercel

Consulta la [Guía de Despliegue](GUIA_DESPLIEGUE.md).

---

## 📁 Estructura del Proyecto

```
Biblioteca_Virtual/
├── app.py                  # Servidor Flask (aplicación principal)
├── vercel.json             # Configuración de despliegue en Vercel
├── requirements.txt        # Dependencias de Python
├── .env.example            # Plantilla de variables de entorno
├── .gitignore              # Archivos excluidos del repositorio
├── libros.json             # Base de datos local de libros
├── sugerencias.json        # Almacenamiento local de sugerencias
├── README.md               # Documentación del proyecto
├── GUIA_DESPLIEGUE.md      # Guía paso a paso de despliegue
│
├── templates/
│   └── index.html          # Plantilla principal de la interfaz
│
├── static/
│   ├── css/
│   │   └── style.css       # Hoja de estilos
│   ├── js/
│   │   └── script.js       # Lógica del lado del cliente
│   └── img/
│       └── libros/         # Portadas de los libros
│
└── docs/                   # Documentación técnica del proyecto
    ├── Manual_Biblioteca_Virtual_Leonardo_Infante.pdf
    ├── Manual_Tecnico_Actualizado.md
    ├── Manual_Tecnico_Actualizado.pdf
    ├── Diagramas_Actualizados.md
    ├── Diagramas_Sistema_Actualizado.pdf
    ├── Diagramas_de_Flujo_Sistema_Biblioteca.pdf
    └── Guia_Despliegue_Vercel.pdf
```

---

## 📄 Documentación Técnica

En la carpeta `docs/` se encuentra la documentación completa del proyecto, que incluye:

- **Manual de usuario** — Instrucciones de uso de la plataforma para estudiantes y docentes.
- **Manual técnico** — Descripción de la arquitectura, componentes y funcionamiento interno del sistema.
- **Diagramas del sistema** — Diagramas de flujo y de arquitectura que ilustran el comportamiento de la aplicación.
- **Guía de despliegue** — Procedimiento para publicar la aplicación en producción.

---

## 👥 Autores

Proyecto de **Servicio Comunitario** desarrollado por estudiantes del **Instituto Universitario Politécnico Santiago Mariño (IUPSM)**, 2026.

**Comunidad beneficiada:** Complejo Educativo Leonardo Infante — Campo Rico, Petare, Caracas, Venezuela.

---

## 📄 Licencia

Proyecto académico desarrollado con fines educativos y de servicio comunitario. Uso libre para la comunidad del Complejo Educativo Leonardo Infante.
