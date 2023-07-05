import API
import requests
import datetime
import json


class FlightSearch:
    """This class is responsible for talking to the Flight Search API."""
    def __init__(self):
        self.tequila_endpoint = 'https://api.tequila.kiwi.com'
        self.tequila_header = {
            'apikey': API.tequila_apikey
        }

    def IATA_search(self, city_name: str) -> str:
        """Return the IATA code of input city"""
        print(f'{city_name} IATA search')
        query = {
            'term': city_name,
            'location_types': 'city'
        }
        response = requests.get(url=f'{self.tequila_endpoint}/locations/query',
                                headers=self.tequila_header, params=query)
        # print(json.dumps(response.json(), indent=4))
        # print(response.json(), type(response.json()))
        city_code = response.json()['locations'][0]['code']
        print(f'{city_name} city code: {city_code}')
        return city_code

    def find_cheap_flights_to(self,  arrival: str, departure='LON',) -> dict:
        """Return the data as a dict.
        Example
        {
            "id": "204525c34ce300003385de2c_0|0a7c22f54cf0000003a719fe_0",
            "flyFrom": "SEN",
            "flyTo": "CDG",
            "cityFrom": "London",
            "cityCodeFrom": "LON",
            "cityTo": "Paris",
            "cityCodeTo": "PAR",
            "countryFrom": {
                "code": "GB",
                "name": "United Kingdom"
            },
            "countryTo": {
                "code": "FR",
                "name": "France"
            },
            "nightsInDest": 13,
            "quality": 105.153653,
            "distance": 314.09,
            "duration": {
                "departure": 4200,
                "return": 3900,
                "total": 8100
            },
            "price": 54,
            "conversion": {
                "EUR": 63.153758,
                "GBP": 54
            },
            "fare": {
                "adults": 54,
                "children": 54,
                "infants": 54
            },
            "bags_price": {
                "1": 100.5
            },
            "baglimit": {
                "hand_height": 40,
                "hand_length": 55,
                "hand_weight": 10,
                "hand_width": 20,
                "hold_dimensions_sum": 158,
                "hold_height": 52,
                "hold_length": 78,
                "hold_weight": 15,
                "hold_width": 28,
                "personal_item_height": 30,
                "personal_item_length": 40,
                "personal_item_weight": 10,
                "personal_item_width": 20
            },
            "availability": {
                "seats": null
            },
            "airlines": [
                "VY",
                "U2"
            ],
            "route": [
                {
                    "id": "204525c34ce300003385de2c_0",
                    "combination_id": "204525c34ce300003385de2c",
                    "flyFrom": "SEN",
                    "flyTo": "CDG",
                    "cityFrom": "London",
                    "cityCodeFrom": "LON",
                    "cityTo": "Paris",
                    "cityCodeTo": "PAR",
                    "airline": "U2",
                    "flight_no": 4646,
                    "operating_carrier": "EC",
                    "operating_flight_no": "",
                    "fare_basis": "",
                    "fare_category": "M",
                    "fare_classes": "",
                    "fare_family": "",
                    "return": 0,
                    "bags_recheck_required": false,
                    "vi_connection": false,
                    "guarantee": false,
                    "equipment": null,
                    "vehicle_type": "aircraft",
                    "local_arrival": "2023-11-22T16:45:00.000Z",
                    "utc_arrival": "2023-11-22T15:45:00.000Z",
                    "local_departure": "2023-11-22T14:35:00.000Z",
                    "utc_departure": "2023-11-22T14:35:00.000Z"
                },
                {
                    "id": "0a7c22f54cf0000003a719fe_0",
                    "combination_id": "0a7c22f54cf0000003a719fe",
                    "flyFrom": "ORY",
                    "flyTo": "LGW",
                    "cityFrom": "Paris",
                    "cityCodeFrom": "PAR",
                    "cityTo": "London",
                    "cityCodeTo": "LON",
                    "airline": "VY",
                    "flight_no": 6944,
                    "operating_carrier": "VY",
                    "operating_flight_no": "6944",
                    "fare_basis": "DOWVYLB",
                    "fare_category": "M",
                    "fare_classes": "D",
                    "fare_family": "",
                    "return": 1,
                    "bags_recheck_required": false,
                    "vi_connection": false,
                    "guarantee": false,
                    "equipment": null,
                    "vehicle_type": "aircraft",
                    "local_arrival": "2023-12-05T17:30:00.000Z",
                    "utc_arrival": "2023-12-05T17:30:00.000Z",
                    "local_departure": "2023-12-05T17:25:00.000Z",
                    "utc_departure": "2023-12-05T16:25:00.000Z"
                }"""
        today = datetime.date.today()
        date_after_180_days = (today + datetime.timedelta(days=180))
        query = {
            'fly_from': departure,
            'fly_to': arrival,
            'date_from': today.strftime('%d/%m/%Y'),
            'date_to': date_after_180_days.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'GBP',
            'one_for_city': 1
        }
        response = requests.get(url=f'{self.tequila_endpoint}/v2/search', headers=self.tequila_header, params=query)
        # print(json.dumps(response.json(), indent=4))
        return response.json()['data'][0]


# test code
# flight_search = FlightSearch()
# flight_search.IATA_search('Paris')
# print(datetime.date.today().strftime('%d/%m/%Y'))
# print(datetime.date.today() + datetime.timedelta(days=180))
# print(type(flight_search.find_cheap_flights_to('PAR')))
"""
{
    "search_id": "f0c5d8a5-5381-92b1-853c-8978595ed554",
    "currency": "GBP",
    "fx_rate": 0.855056,
    "data": [
        {
            "id": "204525c34ce300003385de2c_0|0a7c22f54cf0000003a719fe_0",
            "flyFrom": "SEN",
            "flyTo": "CDG",
            "cityFrom": "London",
            "cityCodeFrom": "LON",
            "cityTo": "Paris",
            "cityCodeTo": "PAR",
            "countryFrom": {
                "code": "GB",
                "name": "United Kingdom"
            },
            "countryTo": {
                "code": "FR",
                "name": "France"
            },
            "nightsInDest": 13,
            "quality": 105.153653,
            "distance": 314.09,
            "duration": {
                "departure": 4200,
                "return": 3900,
                "total": 8100
            },
            "price": 54,
            "conversion": {
                "EUR": 63.153758,
                "GBP": 54
            },
            "fare": {
                "adults": 54,
                "children": 54,
                "infants": 54
            },
            "bags_price": {
                "1": 100.5
            },
            "baglimit": {
                "hand_height": 40,
                "hand_length": 55,
                "hand_weight": 10,
                "hand_width": 20,
                "hold_dimensions_sum": 158,
                "hold_height": 52,
                "hold_length": 78,
                "hold_weight": 15,
                "hold_width": 28,
                "personal_item_height": 30,
                "personal_item_length": 40,
                "personal_item_weight": 10,
                "personal_item_width": 20
            },
            "availability": {
                "seats": null
            },
            "airlines": [
                "VY",
                "U2"
            ],
            "route": [
                {
                    "id": "204525c34ce300003385de2c_0",
                    "combination_id": "204525c34ce300003385de2c",
                    "flyFrom": "SEN",
                    "flyTo": "CDG",
                    "cityFrom": "London",
                    "cityCodeFrom": "LON",
                    "cityTo": "Paris",
                    "cityCodeTo": "PAR",
                    "airline": "U2",
                    "flight_no": 4646,
                    "operating_carrier": "EC",
                    "operating_flight_no": "",
                    "fare_basis": "",
                    "fare_category": "M",
                    "fare_classes": "",
                    "fare_family": "",
                    "return": 0,
                    "bags_recheck_required": false,
                    "vi_connection": false,
                    "guarantee": false,
                    "equipment": null,
                    "vehicle_type": "aircraft",
                    "local_arrival": "2023-11-22T16:45:00.000Z",
                    "utc_arrival": "2023-11-22T15:45:00.000Z",
                    "local_departure": "2023-11-22T14:35:00.000Z",
                    "utc_departure": "2023-11-22T14:35:00.000Z"
                },
                {
                    "id": "0a7c22f54cf0000003a719fe_0",
                    "combination_id": "0a7c22f54cf0000003a719fe",
                    "flyFrom": "ORY",
                    "flyTo": "LGW",
                    "cityFrom": "Paris",
                    "cityCodeFrom": "PAR",
                    "cityTo": "London",
                    "cityCodeTo": "LON",
                    "airline": "VY",
                    "flight_no": 6944,
                    "operating_carrier": "VY",
                    "operating_flight_no": "6944",
                    "fare_basis": "DOWVYLB",
                    "fare_category": "M",
                    "fare_classes": "D",
                    "fare_family": "",
                    "return": 1,
                    "bags_recheck_required": false,
                    "vi_connection": false,
                    "guarantee": false,
                    "equipment": null,
                    "vehicle_type": "aircraft",
                    "local_arrival": "2023-12-05T17:30:00.000Z",
                    "utc_arrival": "2023-12-05T17:30:00.000Z",
                    "local_departure": "2023-12-05T17:25:00.000Z",
                    "utc_departure": "2023-12-05T16:25:00.000Z"
                }
            ],
            "booking_token": "GExl7AFZwn6lG_xwNA69LMpIMTUgUJad6qtOgpmZohEfUKwUSqMKL5rLN7UwaLQDV5eRe9jcQtlE2x3OlyeykYMqWcq6klHdjr5XUYfYw_sSYW3rb2E0k3SqUqpfWfyiIu4b-Lp0Wx7UELir64fRKWlpt7Z0hqDXe0JsB_j8U5nPNHvzx_cpsYDuar1j0AAjoYOQbfBCUkVjh6Yek9QeYrPTCMYCkEWKAiPJbVc1h0TOM0z8QKvUynoCdHW0FpXDE_5cdtLSRzZ3dUiguitespc6Y8sHHknDCmcaPJ7exjBp2NQpw2yYe9xJm2MwuO7ueIG3ZB6H6p5F-1GHjtSPRf31utj42P6l3Vz2PPXFGtXFMIgw5TUU6iyO_ZTvEr6N_91_VSYwKX8OHPjnd8OsteruZ3OBPFtTSyC9MXBMO8yHs8sp3OkG82J90B7MVDqwCDlUildkQuxtEbEMNyvkmygwGHeAo9UHXZ05qztcVy0EJBTWGR4LRLFWUNkT2MOtLVfgSeCmOekzOv4SIgwX15A==",
            "deep_link": "https://www.kiwi.com/deep?affilid=theverypulseflightsearch&currency=GBP&flightsId=204525c34ce300003385de2c_0%7C0a7c22f54cf0000003a719fe_0&from=SEN&lang=en&passengers=1&to=CDG&booking_token=GExl7AFZwn6lG_xwNA69LMpIMTUgUJad6qtOgpmZohEfUKwUSqMKL5rLN7UwaLQDV5eRe9jcQtlE2x3OlyeykYMqWcq6klHdjr5XUYfYw_sSYW3rb2E0k3SqUqpfWfyiIu4b-Lp0Wx7UELir64fRKWlpt7Z0hqDXe0JsB_j8U5nPNHvzx_cpsYDuar1j0AAjoYOQbfBCUkVjh6Yek9QeYrPTCMYCkEWKAiPJbVc1h0TOM0z8QKvUynoCdHW0FpXDE_5cdtLSRzZ3dUiguitespc6Y8sHHknDCmcaPJ7exjBp2NQpw2yYe9xJm2MwuO7ueIG3ZB6H6p5F-1GHjtSPRf31utj42P6l3Vz2PPXFGtXFMIgw5TUU6iyO_ZTvEr6N_91_VSYwKX8OHPjnd8OsteruZ3OBPFtTSyC9MXBMO8yHs8sp3OkG82J90B7MVDqwCDlUildkQuxtEbEMNyvkmygwGHeAo9UHXZ05qztcVy0EJBTWGR4LRLFWUNkT2MOtLVfgSeCmOekzOv4SIgwX15A==",
            "facilitated_booking_available": true,
            "pnr_count": 2,
            "has_airport_change": false,
            "technical_stops": 0,
            "throw_away_ticketing": false,
            "hidden_city_ticketing": false,
            "virtual_interlining": false,
            "local_arrival": "2023-11-22T16:45:00.000Z",
            "utc_arrival": "2023-11-22T15:45:00.000Z",
            "local_departure": "2023-11-22T14:35:00.000Z",
            "utc_departure": "2023-11-22T14:35:00.000Z"
        }
    ],
    "_results": 1
}
"""

