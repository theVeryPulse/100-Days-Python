# request questions from 'https://opentdb.com/api.php'

import requests
import html
parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url='https://opentdb.com/api.php', params=parameters)
response.raise_for_status()
question_data = response.json()
question_data = question_data['results']
for question in question_data:
    question['question'] = html.unescape(question['question'])