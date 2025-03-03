import streamlit as st
import requests
import re

# Configuración del icono en la pestaña del navegador
st.set_page_config(page_title="LitBot - Recomendador de Libros", page_icon="📚", layout="centered")

# URL del endpoint de FastAPI
url = "http://127.0.0.1:8000/recomendacion"

# Estilo para agregar el fondo
st.markdown(
    """
    <style>
    /* Fondo de toda la página */
    .stApp {
        background-color: #2b4b82;
    }
    /* Color del texto */
    h1, h2, h3, h4, h5, h6, p, div, span, label {
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('''
<div style="position: relative; width: 100%; height: 0; padding-top: 25.0000%;
 padding-bottom: 0; box-shadow: 0 2px 8px 0 rgba(63,69,81,0.16); margin-top: 1.6em; margin-bottom: 0.9em; overflow: hidden;
 border-radius: 8px; will-change: transform;">
  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGggl8jEQo/p1BljB-B16toMb_l5-f94A/watch?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
</div>
''', unsafe_allow_html=True)

# Título con estilo
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #f7b4a7;
            text-align: center;
        }
    </style>
    <div class="title">LitBot - Recomendador de Libros</div>
""", unsafe_allow_html=True)

# Descripción con estilo
st.markdown("""
    <style>
        .description {
            font-size: 20px;
            color:#94ddde;            
            text-align: center;
        }
    </style>
    <div class="description">¡Bienvenido! Escribe lo que te gustaría leer, y LitBot te dará una recomendación de libro.</div>
""", unsafe_allow_html=True)

# Caja de texto donde el usuario puede escribir su consulta con un diseño atractivo
consulta_usuario = st.text_input("¿Qué tipo de libro buscas?", "", placeholder="Por ejemplo, 'asesinatos en el País Vasco'")

# Botón estilizado para hacer la recomendación
if st.button("Obtener recomendación", key="recomendacion_btn"):
    if consulta_usuario:
        # Enviar la consulta al endpoint de FastAPI
        data = {"consulta": consulta_usuario}
        response = requests.post(url, json=data)
        
        # Verificar si la respuesta fue exitosa
        if response.status_code == 200:
            recomendacion = response.json()          
                        
            # Mostrar la recomendación con formato adecuado
            st.write(f"Recomendación: {recomendacion}", unsafe_allow_html=True)
        else:
            st.error("Hubo un error al obtener la recomendación.")
    else:
        st.warning("Por favor ingresa una consulta.")


# Pie de página con un toque más personal
st.markdown("""
    <style>
        .footer {
            font-size: 14px;
            color: #94ddde;
            text-align: center;
        }
    </style>
    <div class="footer">¡LitBot - Tu recomendador de libros! | Hecho con ❤️</div>
""", unsafe_allow_html=True)