import API
import requests
from users_manager import get_user_info
import json


class DataManager:
    """This class is responsible for talking to the Google Sheet."""
    def __init__(self):
        self.SHEETY_HEADERS = {
            'Authorization': API.sheety_auth
        }
        self.sheety_username = API.sheety_username
        self.prices_api_endpoint = f'https://api.sheety.co/{self.sheety_username}/flightDeals/prices'
        self.users_api_endpoint = f'https://api.sheety.co/{self.sheety_username}/flightDeals/users'

    def get_rows_prices_sheet(self) -> list:
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
        response = requests.get(url=self.prices_api_endpoint, headers=self.SHEETY_HEADERS)
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
        response = requests.put(url=f'{self.prices_api_endpoint}/{city_id}',
                                headers=self.SHEETY_HEADERS, json=update_info)
        print(f'Sheety response: {response.text}')

    def get_rows_users_sheet(self) -> list:
        """Get all the data from the table. Return a list containing dict objects.
        [{'firstName': 'Philip', 'lastName': 'Li', 'email': 'philip.test.python@gmail.com', 'id': 2}, {...}]"""
        response = requests.get(url=self.users_api_endpoint, headers=self.SHEETY_HEADERS)
        return response.json()['users']

    def add_new_user(self):
        """Add a new user to the Google sheet 'users'"""
        print('Adding a new user...')
        name_email: dict = get_user_info()
        body = {
            'user': {
                'firstName': name_email['first name'],
                'lastName': name_email['last name'],
                'email': name_email['email'],
            }
        }
        response = requests.post(url=f'https://api.sheety.co/{self.sheety_username}/flightDeals/users',
                                 headers=self.SHEETY_HEADERS, json=body)
        print(f'Sheety response: {response.text}')


# t1 = DataManager()
# t1.add_new_user()


