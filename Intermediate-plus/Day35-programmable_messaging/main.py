## API from https://openweathermap.org

import requests
from twilio.rest import Client
import os

ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = os.getenv("OWM_API_KEY")


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv("TWIL_ACCOUNT_SID")
auth_token = os.getenv("TWIL_AUTH_TOKEN")


PARAMS = {
    'lat': -2.19616,
    'lon':-79.88621,
    'appid': API_KEY,
    'cnt': 4, #12-hour window (3 forecasts in 3 hours each one)
}


try:
    # Hacer la solicitud GET
    response = requests.get(ENDPOINT, params=PARAMS)
    response.raise_for_status()  # Lanza un error si el código de estado no es 200
    # print(response.status_code)
    # print(response)

    # # Convertir la respuesta a JSON
    data = response.json()

    forecast_count = PARAMS['cnt']

    will_rain = False

    for index in range(forecast_count):
        weather_id = data['list'][index]['weather'][0]['id']
        if weather_id < 700:
            will_rain = True

    if will_rain:   

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="Go to read is raining, you have so many books unfinished 📚📚📒.",
            from_='whatsapp:+14155238886',
            to='whatsapp:+51965813852'
        )

        print(message.status)
    
    else:
        print('Go to the beach, bitch!')


except requests.exceptions.RequestException as e:
    print("Error en la solicitud:", e)

