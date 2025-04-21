import requests
from dotenv import load_dotenv
import os
from datetime import datetime


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

exercises_list = result['exercises']

# SHEETY API
sheety_endpoint = "https://api.sheety.co/4ee484cad71541617520838c5dbd3155/myWorkoutApril2025/workouts"

today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

for exercise in exercises_list:    
    exercise_data_input = {
        "workout": {
            "date": today_date,
            "time":	current_time,
            "exercise": exercise.get('name').title(),
            "duration":exercise.get('duration_min'),
            "calories":exercise.get('nf_calories'),
        }
    }


    sheety_response = requests.post(sheety_endpoint , json=exercise_data_input)
    sheety_response.raise_for_status()
    print(sheety_response.status_code)
    print(sheety_response.json())

