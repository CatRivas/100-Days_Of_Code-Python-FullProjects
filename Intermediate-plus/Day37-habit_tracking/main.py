import requests
from dotenv import load_dotenv
import os
from datetime import datetime

# Constants for user and graph identification
USERNAME = 'granito-code'
GRAPH_ID = 'booktracker'

# Load environment variables from .env file
load_dotenv()

# Base URL for Pixela service
pixela_endpoint = "https://pixe.la/v1/users"
API_TOKEN = os.getenv('PIXELA_TOKEN')

# User registration data (only needed once)
user_data = {
    'token': API_TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# Create a new user (uncomment this line if the user hasn't been created yet)
# response = requests.post(url=pixela_endpoint, json=user_data)
# print(response.text)


# Graph creation endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Required headers for authentication
HEADERS = {
    "X-USER-TOKEN": API_TOKEN,
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Daily Pages Read Graph",
    "unit": "commit",  
    "type": "int",
    "color": "ajisai",
}

# Create a new graph (uncomment to create)
# response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
# print(response.text)


# Endpoint to create a new pixel (daily record)
create_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today_date = datetime.now().date()
today_date_formatted = today_date.strftime("%Y%m%d") #required format


point_data = {
    "date": today_date_formatted,
    "quantity": input("How many pages of any book did you read today? "),
}


# Create today's pixel (uncomment to run)
response = requests.post(url=create_pixel_endpoint, json=point_data, headers=HEADERS)
print(response.text)


# Endpoint to update an existing pixel (for today)
update_pixel_endpoint = f"{create_pixel_endpoint}/{today_date_formatted}"

point_update_data = {
    "quantity": "20",
}

# Update today's pixel (uncomment to run)
# response = requests.put(url=update_pixel_endpoint, json=point_update_data, headers=HEADERS)
# print(response.text)


# xxx DELETE PIXEL xxx
chosen_date = "20240413"

# Endpoint to delete a pixel on the selected date
delete_pixel_endpoint = f"{create_pixel_endpoint}/{chosen_date}"

# Delete pixel on the chosen date (uncomment to run)
# response = requests.delete(url=delete_pixel_endpoint, headers=HEADERS)
# print(response.text)
