import json


def generate_notification_from(city_flight: dict, sheet_data_dict) -> list:
    """Generate corresponding texts based on the price of the flights"""
    texts_list = []
    for dst_city in city_flight:
        print(f'==Comparing current price with expectation: {dst_city}==')
        if sheet_data_dict[dst_city].get("lowestPrice") is None:
            continue
        if city_flight[dst_city]['price'] <= sheet_data_dict[dst_city].get("lowestPrice"):
        # if True:  # test mode, use this line to skip comparison
            text = f'Subject:==CHEAP FLIGHT TO {dst_city.upper()}==\n\n' \
                   f'Only £{city_flight[dst_city]["price"]} to fly from ' \
                   f'{city_flight[dst_city]["cityFrom"]}-{city_flight[dst_city]["flyFrom"]} to ' \
                   f'{city_flight[dst_city]["cityTo"]}-{city_flight[dst_city]["flyTo"]}! ' \
                   f'From {city_flight[dst_city]["route"][0]["local_departure"].split("T")[0]} to ' \
                   f'{city_flight[dst_city]["route"][1]["local_departure"].split("T")[0]}'
            # include layovers in the notification
            if len(city_flight[dst_city]['route']) > 2:
                layovers = []
                for flight in city_flight[dst_city]['route']:
                    layovers.append(flight['cityTo'])
                text += f'\nThe complete journey: {"->".join(layovers)}'
            text += f'\n\nGet your ticket now at: {city_flight[dst_city]["deep_link"]}'
            texts_list.append(text)
    for text in texts_list:
        print(text)
    return texts_list


# TEST CODES
# with open('city_flight_data.json', 'r') as file:
#     data = json.load(file)
# generate_notification_from(data, '')