# This program tells user whether the ISS station is above them, and if it is dark for them to see it
# It requests ISS coordinates from the API of http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# It checks sunrise and sunset time from the API of https://sunrise-sunset.org/api
# It recalibrates the hour every 60 minutes; it does not recheck sunset/rise until relaunched
# It bases calculation on the coordinates of London
# Thoughts: sick!
# SKILLS: API
# Difficulty: medium

import requests
from datetime import datetime
import time
import math


def to_hour(sun_status_str: str) -> int:
    """
    Extract the hour from an API response from 'https://api.sunrise-sunset.org/json'

    Expected input format: '2023-06-29T20:23:48+00:00

    output:
    23 -> int"""
    sun_status_str = sun_status_str.split('T')
    sun_status_str = sun_status_str[1].split(':')
    sun_status_str = sun_status_str[0]
    return int(sun_status_str)


# London coordinates
user_lat = 51.507351
user_lng = -0.127758
parameters = {'lat': user_lat, 'lng': user_lng, 'formatted': 0}  # formatted=0 returns 24 hours rather than AM/PMs
print(f'You are at ({round(user_lng, 4)}, {round(user_lat, 4)})')
# ===get the sunset time===
sun_status_response = requests.get(url=f'https://api.sunrise-sunset.org/json', params=parameters)
sun_status_response.raise_for_status()
sun_status_json = sun_status_response.json()
sunset_hour = to_hour(sun_status_json['results']['sunset'])
sunrise_hour = to_hour(sun_status_json['results']['sunrise'])
# print(sun_status_json['results']['sunset'])  # test code
# print(f'sunset: {sunset_hour} {type(sunset_hour)}')  # test code
# print(f'sunrise: {sunrise_hour} {type(sunrise_hour)}')  # test code
# ===get the current hour===
time_now_dt_obj = datetime.now()
hour_now = time_now_dt_obj.hour
print('current hour: ', hour_now)

minutes_since_last_check = 0
# ===display result===
while True:
    # ===get the ISS location===
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    # print(response.status_code)  # test code
    response.raise_for_status()
    data = response.json()
    # print(data)  # test code
    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])
    # print(iss_latitude, iss_longitude)  # test code
    # ===check if it is dark===
    is_dark = True if hour_now < sunrise_hour or hour_now > sunset_hour else False
    # ===check if ISS is within 5 degrees, both in longitude or latitude===
    iss_is_close = True if abs(user_lat - iss_latitude) <= 5 and abs(user_lng - iss_longitude) < 5 else False
    # ===Show the user===
    degree_diff = math.sqrt((user_lat - iss_latitude) ** 2 + (user_lng - iss_longitude) ** 2)
    degree_diff = round(degree_diff, 3)
    if is_dark and iss_is_close:
        print('LOOK ABOVE!')
    else:
        print(f'ISS is at {round(iss_longitude,2)}, {round(iss_latitude, 2)}\n'
              f'Degree difference: {degree_diff}\n'
              f'patience...\n')
    time.sleep(60)
    # Recalibrate the hour every 60 minutes
    minutes_since_last_check += 1
    if minutes_since_last_check % 60 == 0:
        time_now_dt_obj = datetime.now()
        hour_now = time_now_dt_obj.hour
        print('current hour: ', hour_now)
    print(f'program running time: {minutes_since_last_check}m')