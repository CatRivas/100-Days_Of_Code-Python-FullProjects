import requests
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os
import time


# my position 
MY_LAT = 47.6016
MY_LONG = 25.7560

def main():
    while True: 
        if is_dark():
            send_email()
            time.sleep(60) 
            print('Checking again...')
        else:
            print('It is not dark yet...')
            print('Checking again in 30 min...')
            time.sleep(30*60)


def iss_position_against_mine():
# ISS POSITION
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #If the ISS is close to my current position
    #Your position is within +5 or -5 degrees of the ISS position.
    margin = 5
    if abs(iss_latitude- MY_LAT) <= margin and abs(iss_longitude - MY_LONG) <= margin:
        return True
    return False


def is_dark():
    # THE SUNRISE AND SUNSET TIMES OF MY POSITION
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise_hour = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset_hour = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    # it is currently dark?
    return time_now < sunrise_hour or time_now > sunset_hour
    
    
# Then send me an email to tell me to look up.
def send_email(): 
    if iss_position_against_mine():
        load_dotenv()

        sender_email = os.getenv('secret_sender_email')
        sender_password = os.getenv('secret_sender_password')
        receiver_email = os.getenv('secret_receiver_email')
        
        subject = 'ISS ON THE BLOCK!!!'
        text = f'Subject: {subject}\n\nThe ISS is overhead. Look up!!!' 

        try:
            with smtplib.SMTP('smtp.gmail.com', port=587) as server:
                server.starttls()

                server.login(sender_email, sender_password)
                print('Logged in...')

                server.sendmail(from_addr=sender_email, to_addrs=receiver_email, msg=text)

                print(f'Email has been send')
        
        except smtplib.SMTPException as e:
            print(f'Fail to send email, because of {e}')
    else:
        print('No ISS overhead...')


if __name__ == '__main__':

    main()
    

