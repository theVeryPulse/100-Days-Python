import json


def print_pretty_json(json_data):
    """Print in console the argument json data in prettier format"""
    parsed = json_data
    print(json.dumps(parsed, indent=4))