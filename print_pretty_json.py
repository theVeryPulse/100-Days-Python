import json


def print_pretty_json(json_data):
    """Print in console the argument json data in prettier format"""
    print(json.dumps(json_data, indent=4))