import smtplib
import datetime as dt
import random
import pandas as pd

##dotenv for saving environment variables in the project, not in the system
from dotenv import load_dotenv
import os

def main():
    # let's load the .env file
    load_dotenv()

    #now we access the enviroment varibales in the loaded .env file
    sender_email = os.getenv('secret_sender_email')
    sender_password = os.getenv('secret_sender_password')

    csv_path = 'birthdays.csv'
    df = pd.read_csv(csv_path)
 
    current_month, current_day = get_current_date()
    
    receiver_name, receiver_email = find_birthday_person(df, current_month, current_day)
    
    email_body = generate_email_body(receiver_name)

    send_birthday_email(sender=sender_email, receiver=receiver_email, password=sender_password,body=email_body)

    
def get_current_date():
    month = dt.datetime.now().month
    day = dt.datetime.now().day 

    return month, day
    

def find_birthday_person(dataframe, month, day):
    """
    Checks if there is an someone whose birthday is on the given date.
    """

    selected_row = dataframe.loc[(dataframe['month'] == month) & (dataframe['day'] == day)]

    name = selected_row['name'].iloc[0]
    email = selected_row['email'].iloc[0]

    return name, email
    

def generate_email_body(name):
    """
    Generates the body of the birthday email by replacing the placeholder [NAME] with the actual name in the chosen template.
    """

    random_template = random.randint(1, 3)
    path = f'letter_templates/letter_{random_template}.txt'    

    with open(path) as file:
        content = file.readlines() 

    modified_content = [line.replace('[NAME]', name) for line in content]

    return ''.join(modified_content)
    

def send_birthday_email(sender, receiver, password, body): 
    subject = 'HAPPY BDAY!!!'
        
    text = f'Subject: {subject}\n\n{body}'

    try:
        with smtplib.SMTP('smtp.gmail.com', port=587) as server:
            server.starttls()

            server.login(sender, password)
            print('Logged in...')

            server.sendmail(sender, receiver, text)

            print(f'Email has been send to {receiver}')
    
    except smtplib.SMTPException:
        print(f'Fail to send email to {receiver}')


if __name__ == '__main__':
    main()



