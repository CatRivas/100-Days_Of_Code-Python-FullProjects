import requests
from dotenv import load_dotenv
import os

load_dotenv()

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "Content-Type": 'application/json',
    "x-app-id":os.getenv('APP_ID'),
    "x-app-key":os.getenv('API_KEY'),
    "x-remote-user-id": "0",
}


user_exercise = input('Tell me wich exercise you did: ') 

parameters = {
    "query": user_exercise,
    "weight_kg": os.getenv('WEIGHT_KG'),
    "height_cm": os.getenv('HEIGHT_CM'),
    "age": os.getenv('AGE'),
}

# Realizar el POST request
response = requests.post(endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)
