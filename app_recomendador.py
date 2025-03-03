from fastapi import FastAPI, requests, HTTPException, Query
from pydantic import BaseModel
import cohere
import pymysql
import uvicorn
import pandas as pd
from dotenv import load_dotenv
import os


app = FastAPI()


class Consultas(BaseModel):    
    consulta : str 


'''Credenciales.'''

# Cargar las variables de entorno desde .env

load_dotenv()

# Obtener la clave de la BASE DE DATOS.

host = os.getenv("Database_URL")
user = os.getenv("user")
password_db = os.getenv("password_db")

# Obtener la clave de la API.

api_key = os.getenv("cohere_api_key")


'''Mensaje de bienvenida.'''

@app.get("/")
async def hello():
    return "Bienvenidos a LitBot"


'''Endpoint.'''

# Endpoint para la conexion con el LitBot.

@app.post("/recomendacion")
async def obtener_recomendacion(pregunta: Consultas):
    co = cohere.ClientV2(api_key)
    response = co.chat(
        model="command-r-plus",
        messages=[{"role": "system", "content": "eres un lector y quieres que te recomienden un libro"},
              {"role": "user", "content": pregunta.consulta}
         ]        
)
    
    recomendacion = response.message.content[0].text

    db = pymysql.connect(host = host,
                     user = user,
                     password = password_db,
                     port = 3306,
                     cursorclass = pymysql.cursors.DictCursor  
)

    cursor = db.cursor()
    use_db = '''USE recomendador_libros'''
    cursor.execute(use_db)
    query = '''INSERT INTO consultas (consulta, recomendacion)
    VALUES (%s, %s)'''
    cursor.execute(query, (pregunta.consulta, recomendacion))    
    db.commit()
    cursor.close()
    db.close()
    return recomendacion

    
   
'''Ejecutar la aplicación.'''

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    
    








        
    

