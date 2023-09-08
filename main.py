import os

import requests
from dotenv import load_dotenv
from _datetime import datetime

# Load environment variables from .env file
load_dotenv()


# creating constants
USERNAME = "jyotpreet"
TOKEN = os.getenv("PIXELA_API_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "TOKEN",
    "username": "USERNAME",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP 1 - user account has been created


# step 2 - lets create a graph

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"  # how f string used

graph_config = {
    "id": "graph1",
    "name": "Coding tracker graph",
    "unit": "hours",
    "type": "int",
    "color": "momiji"
}

# to authenticate -
headers = {        # created dictionary but why name headers which will late coincide with kwarg headers?
    "X-USER-TOKEN": TOKEN        # our password
}

# response = requests.post(url = graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# step 4 - post value to the graph

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# today = datetime(year=2023, month=9, day=7)  if you want to change the record of a said date

# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today?"),
}

# reuse the headers to authenticate

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# update an old record

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "1"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# deleting a record

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)





