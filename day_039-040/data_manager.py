import API
import requests
import json


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.SHEETY_HEADERS = {
            'Authorization': API.sheety_auth
        }
        self.sheety_username = API.sheety_username
        self.api_endpoint = f'https://api.sheety.co/{self.sheety_username}/flightDeals/prices'

    def get_rows(self) -> list:
        """Get all the data from the table. Return a list containing dict objects.
        [
            {
                "city": "Paris",
                "iataCode": "",
                "lowestPrice": 54,
                "id": 2
            },
            {
                "city": "Berlin",
                "iataCode": "",
                "lowestPrice": 42,
                "id": 3
            },
            ...
        ]"""
        response = requests.get(url=self.api_endpoint, headers=self.SHEETY_HEADERS)
        return response.json()['prices']

    def update_iata(self, city_id: int, city_code: str):
        """Update the IATA codes of target city. Input the city as in ['id']

        Name of the record that needs changing must match the name of the key in the returned data"""
        print('.update_iata()')
        update_info = {
            'price': {
                'iataCode': city_code
            }
        }
        response = requests.put(url=f'{self.api_endpoint}/{city_id}', headers=self.SHEETY_HEADERS, json=update_info)
        print(f'Sheety response: {response.text}')

# data_manager = DataManager()
# data_manager.get_rows()

