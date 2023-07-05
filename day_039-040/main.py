# This program checks the lowest price of flights from London to other cities
# When the flight is cheaper than the preset value, it sends an SMS to notify the user
# Difficulty: hard


from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import json

print('039-040')
notification_manager = NotificationManager()
flight_search = FlightSearch()
data_manager = DataManager()
sheet_data = data_manager.get_rows()
sheet_data_dict = {city['city']: city for city in sheet_data}
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
# print(sheet_data, type(sheet_data))

# Fill in the IATA city codes if not already exists
for city in sheet_data:
    # print(city.keys())  # test code
    if city['iataCode'] == '':
        city_code = flight_search.IATA_search(city['city'])
        data_manager.update_iata(city_id=city['id'], city_code=city_code)


# Check low price flights
data_summary = {}
for city in sheet_data:
    print(f'Checking flights to {city["city"]}')
    data_summary[city["city"]] = flight_search.find_cheap_flights_to(city['iataCode'])

# print(data_summary.keys())
# if the ticket price is lower than the preset value, send an SMS to notify the user
for dst_city in data_summary:
    if data_summary[dst_city]['price'] <= sheet_data_dict[dst_city]["lowestPrice"]:
        text = f'Only £{data_summary[dst_city]["price"]} to fly from ' \
               f'{data_summary[dst_city]["cityFrom"]}-{data_summary[dst_city]["flyFrom"]} to ' \
               f'{data_summary[dst_city]["cityTo"]}-{data_summary[dst_city]["flyTo"]}! ' \
               f'From {data_summary[dst_city]["route"][0]["local_departure"].split("T")[0]} to ' \
               f'{data_summary[dst_city]["route"][1]["local_departure"].split("T")[0]}'
        print(text)
        notification_manager.send_msg(text)