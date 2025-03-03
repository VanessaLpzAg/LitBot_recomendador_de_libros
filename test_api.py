import requests

def test_obtener_recomendacion():
    url = "http://127.0.0.1:8000/recomendacion"
    data = {"consulta": "quiero libros ambientados en el pais vasco sobre asesinatos y mitologia vasca"}    
    response = requests.post(url, json=data)       
    assert response.status_code == 200  
    assert isinstance(response.json(), str)

# Ejecutar el test
if __name__ == "__main__":
    test_obtener_recomendacion()