import os
import requests
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Obtener variables del entorno
IATA_CODE = "LIM"
API_KEY = os.getenv("API_KEY")
API_ENPOINT = os.getenv("API_URL")

def make_request():
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(API_ENPOINT, headers=headers)
        response.raise_for_status()  # Lanza error si la respuesta es 4xx o 5xx
        data = response.json()
        print("✅ Datos recibidos:", data)
    except requests.exceptions.HTTPError as errh:
        print("❌ Error HTTP:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("❌ Error de conexión:", errc)
    except requests.exceptions.Timeout as errt:
        print("❌ Timeout:", errt)
    except requests.exceptions.RequestException as err:
        print("❌ Otro error:", err)

if __name__ == "__main__":
    make_request()
