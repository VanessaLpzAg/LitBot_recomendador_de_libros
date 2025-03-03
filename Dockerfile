# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app

# Instalar las dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Crear un entorno virtual (opcional pero recomendado)
RUN python -m venv /env

# Activar el entorno virtual e instalar las dependencias de Python
RUN /env/bin/pip install --upgrade pip && \
    /env/bin/pip install -r requirements.txt

# Exponer el puerto en el que FastAPI está ejecutándose
EXPOSE 8000

# Establecer la variable de entorno para ejecutar FastAPI
ENV PATH="/env/bin:$PATH"

# Comando para ejecutar la aplicación con Uvicorn
CMD ["sh", "-c", "uvicorn my_app:app --host 0.0.0.0 --port 8000 & streamlit run app_streamlit.py --server.port 8501"]