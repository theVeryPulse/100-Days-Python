# This program checks the lowest price of return flights between London and other cities
# The range is from now to six months later, the stay is 7 to 30 days long
# When the flight is cheaper than the preset value, it sends an SMS or email to notify the registered users
# Preset prices and registered users are accessed and saved in google sheet through Sheety API
# Flight price information are inquired from kiw.com API
# SKILLS: API
# Difficulty: HARD


from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from message_generator import generate_notification_from
import json

print('039-040')
notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
# ===get preset price from Google sheet===
prices_sheet_data = data_manager.get_rows_prices_sheet()
"""sheet_data example:
[
    {
        "city": "Paris",
        "iataCode": "PAR",
        "lowestPrice": 54,
        "id": 2
    },
    {
        "city": "Berlin",
        "iataCode": "BER",
        "lowestPrice": 42,
        "id": 3
    },...
]"""
# ---convert to dict with city name as key---
sheet_data_dict = {city['city']: city for city in prices_sheet_data}

# ===Fill in the IATA city codes if not already exists===
for city in prices_sheet_data:
    # print(city.keys())  # test code
    if city['iataCode'] == '':
        city_code = flight_search.IATA_search(city['city'])
        data_manager.update_iata(city_id=city['id'], city_code=city_code)

# ===Find low price flights===
city_flight = {}
"""
Key: city name, e.g. Paris; 
value: flight information;
"""
for city in prices_sheet_data:
    print(f'Checking flights to {city["city"]}')
    city_flight[city["city"]] = flight_search.find_cheap_flights_to(city['iataCode'])

# ===Generate notif texts of low price===
texts_to_send = generate_notification_from(city_flight=city_flight, sheet_data_dict=sheet_data_dict)

# ===Send the email to clients===
users_info_list = data_manager.get_rows_users_sheet()
for text in texts_to_send:
    for recipient in users_info_list:
        notification_manager.send_emails(text=text.encode('utf-8'), to=recipient['email'])

# ===Alternative: send an SMS to notify the user===
# for text in texts_to_send:
#     notification_manager.send_msg(text)