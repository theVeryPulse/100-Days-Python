# This program tracks the habit with the help of Pixela
# It sevres as an agent for Pixela's API
# User can record, modify, and deletes tracking records
# SKILLS: API, requests, headers
# Difficulty: easy
import requests
import datetime
from login_info import pixela_token, pixela_username


# ===register a user===
pixela_endpoint = 'https://pixe.la/v1/users'
pixela_parameters = {
    'token': pixela_token,
    'username': pixela_username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)


# ===Create a new graph===
create_graph_ep = f'{pixela_endpoint}/{pixela_username}/graphs'
graph_config = {
    'id': 'graph1',
    'name': 'programming',
    'unit': 'hour',
    'type': 'int',
    'color': 'shibafu'
}
HEADER = {'X-USER-TOKEN': pixela_token}
# response = requests.post(url=create_graph_ep, json=graph_config, headers=HEADER)


# ===register to today's track on graph1===
hours_to_add: int = 2
add_pixel_ep = f'{pixela_endpoint}/{pixela_username}/graphs/{graph_config["id"]}'
date_today = datetime.date.today()
add_pixel_param = {
    'date': date_today.strftime('%Y%m%d'),
    'quantity': f'{hours_to_add}'
}
# response = requests.post(url=add_pixel_ep, json=add_pixel_param, headers=HEADER)


# ===update a registered record (HTTP put)===
target_date: str = '20230704'
new_quantity = 1
update_pixel_ed = f'{pixela_endpoint}/{pixela_username}/graphs/{graph_config["id"]}/{target_date}'
update_pixel_param = {'quantity': f'{new_quantity}'}
# response = requests.put(url=update_pixel_ed, json=update_pixel_param, headers=HEADER)


# ===delete a record on target date (HTTP delete)===
target_delete_date: str = '20230704'
delete_pixel_ed = f'{pixela_endpoint}/{pixela_username}/graphs/{graph_config["id"]}/{target_delete_date}'
# response = requests.delete(url=delete_pixel_ed, headers=HEADER)
# print(response.text)