# 100DaysOfPython
import requests

BASE_URL = "https://pixe.la"
TOKEN = "100DaysOfPython"
HEADER = {
        "X-USER-TOKEN": TOKEN
    }


def post_request(endpoint, body, headers=None):
    response = requests.post(url=f'{BASE_URL}{endpoint}', json=body, headers=headers)
    response.raise_for_status()
    print(response.text)


def create_user():
    api_endpoint = '/v1/users'
    username = input("Enter a username: ")
    request_body = {
        "token": TOKEN,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    post_request(api_endpoint, request_body)


def create_graph():
    username = input("Create graph for what username? ")
    graph_id = input("Enter a graph id: ")
    graph_name = input("Enter a name for the graph: ")
    graph_unit = input("Enter your unit of measurement name: ")
    graph_type = input("Unit quantity (int/float)? ")
    graph_color = input("Color (shibafu, momiji, sora, ichou, ajisai, kuro): ")
    api_endpoint = f'/v1/users/{username}/graphs'
    request_body = {
        "id": graph_id,
        "name": graph_name,
        "unit": graph_unit,
        "type": graph_type,
        "color": graph_color
    }
    post_request(api_endpoint, request_body, HEADER)


def post_a_pixel():
    username = input("Record for what username? ")
    graph_id = input("What is the graph ID? ")
    graph_date = input("Enter date (YYYYMMDD): ")
    graph_quantity = input("What is the quantity (int=0-9, float=0-9.0-9)? ")
    api_endpoint = f'/v1/users/{username}/graphs/{graph_id}'
    request_body = {
        "date": graph_date,
        "quantity": graph_quantity
    }
    post_request(api_endpoint, request_body, HEADER)


while True:
    user_response = input("What would you like to do? ").lower()
    if user_response == "exit":
        exit()
    elif user_response == "create user":
        create_user()
    elif user_response == "create graph":
        create_graph()
    elif user_response == "post a pixel":
        post_a_pixel()
    else:
        print("\nOops, that's not an option\n")

