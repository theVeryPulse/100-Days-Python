# This is a workout tracking program
# User can input natural sentences to tell their exercises
# Program uses Nutritionix to interpret the sentences
# It then saves your workout data in a Google spreadsheet through Sheety API
# SKILLS: API, authentication, HTTP post, HTTP header
# Difficulty: medium
import json
import requests
import datetime
from login_info import *

# ===Get the workout information===
NUTRI_HEADERS = {
    'x-app-id': nutritionix_id,
    'x-app-key': nutritionix_key,
    'x-remote-user-id': '0'
}
"""
\"Required HEADERS when accessing Nutritionix V2 API endpoints:
- x-app-id: Your app ID issued from developer.nutritionix.com)
- x-app-key: Your app key issued from developer.nutritionix.com)
- x-remote-user-id:  A unique identifier to represent the end-user who is accessing the Nutritionix API.  
    If in development mode, set this to 0.  
    This is used for billing purposes to determine the number of active users your app has.\"
"""
exercise_description = input('What exercises did you do?\n')
nutri_request = {
    "query": exercise_description,
    "gender": my_info['gender'],
    "weight_kg": my_info['weight_kg'],
    "height_cm": my_info['height_cm'],
    "age": my_info['age']
}
nutri_response = requests.post(url='https://trackapi.nutritionix.com/v2/natural/exercise',
                               headers=NUTRI_HEADERS, json=nutri_request)
exercises = nutri_response.json()['exercises']
"""E.g. [
    {
        "tag_id": 317,
        "user_input": "ran",
        "duration_min": 50.03,
        "met": 9.8,
        "nf_calories": 572.01,
        "photo": {
            "highres": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg",
            "thumb": "https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg",
            "is_user_uploaded": false
        },
        "compendium_code": 12050,
        "name": "running",
        "description": null,
        "benefits": null
    },
    {...}
]"""
# print(json.dumps(nutri_response.json(), indent=4))
print(json.dumps(exercises, indent=4))

# ===Add information to Google sheet===
SHEETY_HEADERS = {
    "Authorization": sheety_auth,
    "Content-Type": "application/json"
}
today_Date = datetime.date.today()
date_today = today_Date.strftime('%d/%m/%Y')
current_hour = datetime.datetime.now().strftime("%X")
sheety_url = f'https://api.sheety.co/{sheety_username}/myWorkouts/workouts'
"""E.g. https://api.sheety.co/username/projectName/sheetName"""
print(current_hour, type(current_hour))
for exercise in exercises:
    sheety_request = {
        'workout': {
            'date': date_today,
            'time:': current_hour,
            'exercise': exercise['name'].title(),
            'duration': exercise['duration_min'],
            'calories': exercise['nf_calories']
        }
    }
    # add a row
    sheety_response = requests.post(url=sheety_url, headers=SHEETY_HEADERS, json=sheety_request)
    print(sheety_response.text)
