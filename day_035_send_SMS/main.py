"""
This program checks the next 12 hours' weather in London (my location);
- If there is bad weather, it will send an SMS to my phone number;
- SMS is supported by Twilio, weather information is from OpenWeatherMap;
- The code is also hosted on Python Anywhere
SKILLS: API with keys, environment variables;
Difficulty: easy;
"""

import requests
import os
from twilio.rest import Client
from log_in_information_private import account_sid, auth_token

# ===get weather forecast===
forecast_endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
onecall_endpoint = 'https://api.openweathermap.org/data/2.5/onecall'  #
parameters = {
    'lat': 51.5072,
    'lon': 0.1276,
    'exclude': 'current,minutely,daily',
    'appid': '',
}

response = requests.get(url=forecast_endpoint, params=parameters)
response.raise_for_status()
print(response.status_code)
if response.status_code == 200:
    print('Request successful')

hourly_weather_list = response.json()['list']
should_bring_umbrella = False
for i in range(5):
    print(hourly_weather_list[i]['weather'][0]['id'])  # test code
    if hourly_weather_list[i]['weather'][0]['id'] < 800:
        should_bring_umbrella = True

# See http://twil.io/secure
client = Client(account_sid, auth_token)

# ===send information to phone, if will rain===
if should_bring_umbrella:
    message = client.messages \
        .create(
            body="Bring an umbrella: it might rain!",
            from_='+447481337415',
            to='+447732234051'
        )
    print(message.status)
else:
    print('You don\'t need to bring an umbrella')
