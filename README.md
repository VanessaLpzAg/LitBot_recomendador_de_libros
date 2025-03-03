# LitBot - Recomendador de Libros con IA 📚🤖

![LitBot Image](./img/Icono_LitBot3.png)

LitBot es un recomendador de libros basado en inteligencia artificial (IA) que interactúa con los usuarios mediante preguntas sobre sus preferencias literarias. Utiliza el modelo de lenguaje de **Cohere** para generar recomendaciones personalizadas de libros y guarda el historial de consultas en una base de datos MySQL para ofrecer un seguimiento más preciso de las recomendaciones.

## 🚀 Tecnologías utilizadas.

- **Python 3.x**: El lenguaje de programación principal para el backend de la aplicación.
- **FastAPI**: Framework para crear la API web que maneja las interacciones con el usuario.
- **Cohere**: API de inteligencia artificial utilizada para generar recomendaciones de libros basadas en el texto proporcionado por el usuario.
- **MySQL**: Base de datos relacional utilizada para almacenar el historial de consultas y recomendaciones de libros.
- **Docker**: Conteneriza la aplicación para su ejecución en cualquier entorno.
- **Docker Compose**: Orquesta los contenedores de la aplicación y la base de datos MySQL.
- **Streamlit**: Framework para crear interfaces de usuario interactivas de manera rápida y sencilla, usado para interactuar con LitBot.

## 📖 Descripción.

LitBot es un servicio web donde los usuarios pueden consultar sobre libros que podrían interesarles. Al recibir una pregunta relacionada con los gustos literarios del usuario, LitBot utiliza la API de **Cohere** para generar una recomendación de libro. Luego, guarda tanto la consulta como la recomendación en una base de datos MySQL para futuras consultas.

Ahora también puedes acceder a una interfaz interactiva utilizando **Streamlit** para enviar tus consultas directamente desde tu navegador.

## 📋 Requisitos.

Antes de ejecutar LitBot, asegúrate de tener los siguientes requisitos:

- Docker y Docker Compose instalados en tu máquina.
- Una cuenta de Cohere y una clave API válida.
- Un archivo `.env` con las credenciales necesarias.
- **Streamlit** instalado en tu entorno de desarrollo si deseas usar la interfaz de usuario interactiva.

## ⚡ Instalación.

### Paso 1: Clonar el repositorio.

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/LitBot.git
cd LitBot
```

### Paso 2: Crear el archivo .env

Crea un archivo .env en el directorio raíz de tu proyecto y agrega las siguientes variables de entorno con tus credenciales:

```bash
Database_URL=mysql:3306
user=root
password_db=mysecretpassword
cohere_api_key=your_cohere_api_key
```

- **Database_URL**: URL de conexión a la base de datos (por defecto mysql:3306).
- **user**: Usuario de MySQL (por defecto root).
- **password_db**: Contraseña para acceder a MySQL.
- **cohere_api_key**: Tu clave API de Cohere.

### Paso 3: Ejecutar la aplicación Streamlit (opcional).

Si prefieres interactuar con LitBot usando una interfaz de usuario, puedes ejecutar la aplicación Streamlit que se incluye en el proyecto. Para hacerlo, asegúrate de tener Streamlit instalado en tu entorno:

```bash
pip install streamlit
```

Luego, ejecuta el siguiente comando:

```bash
streamlit run app_streamlit.py
```

Esto abrirá una interfaz en tu navegador en http://localhost:8501, donde podrás enviar consultas y ver las recomendaciones de libros.

### Paso 4: Ejecutar los contenedores.

Con Docker y Docker Compose instalados, puedes construir y ejecutar los contenedores usando:

```bash
docker-compose up --build
```

Esto construirá y levantará los contenedores de la aplicación y la base de datos MySQL. La aplicación estará disponible en http://localhost:8000.

### Paso 5: Acceder a la aplicación.

Una vez que los contenedores estén corriendo, podrás interactuar con LitBot:

- 👋 Endpoint de bienvenida: Visita http://localhost:8000/ para ver el mensaje de bienvenida.
- 📚 Endpoint de recomendación: Utiliza el endpoint POST /recomendacion para enviar consultas y obtener recomendaciones de libros.


## 💡 Uso Endpoint de API.

1. Realizar una consulta: Puedes realizar una consulta enviando un POST al endpoint /recomendacion con un cuerpo de solicitud en formato JSON, como este:

```bash
{
  "consulta": "Quiero un libro de ciencia ficción"
}
```

LitBot responderá con una recomendación de libro basada en tu consulta.

2. 🗂️ Historial de consultas: Las consultas y recomendaciones se almacenarán en la base de datos MySQL, lo que permite tener un historial de las interacciones.

## 🏗️ Arquitectura.

LitBot está compuesto por dos servicios principales:

1. Servicio FastAPI (litbot): Maneja las solicitudes HTTP, interactúa con Cohere para generar las recomendaciones y gestiona la conexión a la base de datos.

2. Servicio MySQL (mysql): Almacena el historial de consultas y recomendaciones de libros.

Ambos servicios están orquestados mediante Docker Compose, lo que facilita su despliegue y administración.

