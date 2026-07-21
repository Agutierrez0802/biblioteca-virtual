 Biblioteca Virtual Leonardo Infante

Biblioteca digital escolar desarrollada como proyecto de servicio comunitario para el Complejo Educativo Leonardo Infante, ubicado en Campo Rico, Petare, Caracas - Venezuela.

Su proposito es facilitar a los estudiantes de educacion secundaria el acceso gratuito a sus libros de texto en formato digital (PDF), organizados por materia y año escolar, disponibles desde cualquier dispositivo con conexion a internet.

---

 Objetivo del Proyecto

Brindar una herramienta tecnologica que permita a la comunidad estudiantil del Complejo Educativo Leonardo Infante consultar y descargar sus libros de texto de manera sencilla, eliminando la barrera del acceso fisico al material bibliografico.

Este proyecto nace como parte del requisito de Servicio Comunitario del Instituto Universitario Politecnico Santiago Mariño (IUPSM), con el fin de aportar una solucion real a una necesidad de la comunidad educativa.

---

 Funcionalidades

- Catalogo de libros - Mas de 35 libros de texto de la Coleccion Bicentenario, organizados por materia y año escolar (1ro a 5to año).
- Busqueda por titulo - Barra de busqueda para encontrar libros rapidamente por nombre.
- Filtros por materia y año - Filtrado dinamico por area de conocimiento y nivel academico.
- Formulario de sugerencias - Los usuarios pueden sugerir libros que desean que se agreguen al catalogo.
- Modo oscuro - Alternancia entre tema claro y oscuro para una lectura comoda.
- Diseño responsivo - Interfaz adaptable a computadoras, tabletas y telefonos moviles.
- Reloj en tiempo real - Visualizacion de la hora actual en la interfaz.

---

 Catalogo de Materias

El catalogo incluye libros de las siguientes areas de conocimiento:

Materia                        | Años disponibles
-------------------------------|------------------
Ciencias Naturales             | 1ro, 2do, 3ro, 4to, 5to
Ciencias Sociales              | 1ro, 2do, 3ro, 4to, 5to
Matematica                     | 1ro, 2do, 3ro, 4to, 5to
Lengua y Literatura            | 1ro, 2do, 3ro, 4to, 5to
Ingles                         | 1ro, 2do, 3ro, 4to, 5to
Artes (Educacion Artistica)    | 1ro, 2do

Los libros estan alojados en Google Drive y pueden consultarse directamente en linea desde el navegador.

---

 Tecnologias Utilizadas

Componente              | Tecnologia
------------------------|---------------------------
Backend                 | Python 3.13 + Flask 3.1
Frontend                | HTML5, CSS3, JavaScript
Base de Datos           | MongoDB Atlas (con respaldo en archivos JSON locales)
Motor de plantillas     | Jinja2
Despliegue              | Vercel (Serverless Functions)
Control de versiones    | Git + GitHub

---

 Instalacion Local

Prerrequisitos:
- Python 3.10 o superior
- pip (gestor de paquetes de Python)
- Git

Pasos de instalacion:

1. Clonar el repositorio
   git clone https://github.com/Agutierrez0802/biblioteca-virtual.git
   cd biblioteca-virtual

2. Crear un entorno virtual
   python -m venv venv

3. Activar el entorno virtual
   Windows:    venv\Scripts\activate
   Linux/Mac:  source venv/bin/activate

4. Instalar las dependencias
   pip install -r requirements.txt

5. Configurar las variables de entorno
   cp .env.example .env
   Editar el archivo .env con la URI de conexion a MongoDB Atlas.
   Si no se configura, la aplicacion funcionara en modo local utilizando los archivos JSON incluidos.

6. Ejecutar la aplicacion
   python app.py
   La aplicacion estara disponible en http://localhost:5000

---

 Despliegue en Vercel

La aplicacion esta configurada para desplegarse en Vercel como una Serverless Function de Python.

---

 Estructura del Proyecto

Biblioteca_Virtual/
|-- app.py                  # Servidor Flask (aplicacion principal)
|-- vercel.json             # Configuracion de despliegue en Vercel
|-- requirements.txt        # Dependencias de Python
|-- .env.example            # Plantilla de variables de entorno
|-- .gitignore              # Archivos excluidos del repositorio
|-- libros.json             # Base de datos local de libros
|-- sugerencias.json        # Almacenamiento local de sugerencias
|-- README.txt              # Documentacion del proyecto
|
|-- templates/
|   +-- index.html          # Plantilla principal de la interfaz
|
|-- static/
|   |-- css/
|   |   +-- style.css       # Hoja de estilos
|   |-- js/
|   |   +-- script.js       # Logica del lado del cliente
|   +-- img/
|       +-- libros/         # Portadas de los libros
|
+-- docs/                   # Documentacion tecnica del proyecto
    |-- Manual_Biblioteca_Virtual_Leonardo_Infante.pdf
    |-- Manual_Tecnico_Actualizado.pdf
    |-- Diagramas_Sistema_Actualizado.pdf
    |-- Diagramas_de_Flujo_Sistema_Biblioteca.pdf
    +-- Guia_Despliegue_Vercel.pdf

---

 Documentacion Tecnica

En la carpeta docs/ se encuentra la documentacion completa del proyecto, que incluye:

- Manual de usuario - Instrucciones de uso de la plataforma para estudiantes y docentes.
- Manual tecnico - Descripcion de la arquitectura, componentes y funcionamiento interno del sistema.
- Diagramas del sistema - Diagramas de flujo y de arquitectura que ilustran el comportamiento de la aplicacion.
- Guia de despliegue - Procedimiento para publicar la aplicacion en produccion.

---

 Autores

Proyecto de Servicio Comunitario desarrollado por estudiantes del Instituto Universitario Politecnico Santiago Mariño (IUPSM), 2026.

Comunidad beneficiada: Complejo Educativo Leonardo Infante - Campo Rico, Petare, Caracas, Venezuela.

---

 Licencia

Proyecto academico desarrollado con fines educativos y de servicio comunitario. Uso libre para la comunidad del Complejo Educativo Leonardo Infante.