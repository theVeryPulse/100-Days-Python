# This is a stock trading news alert
# When there is a stock price change of over 5%, this program finds the latest news about the company and send it by SMS
# Stock price comes from Alpha Vantage API
# News comes from News Catcher API
# SMS is sent through Twilio API
# SKILLS: API, API authentication
# Difficulty: hard

import requests
from apikeys import alphavantage_apikey, NewsCatcher_apikey, twilio_auth_token, twilio_account_sid
from twilio.rest import Client

print('036')
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# ===STOCK INFORMATION===
# Request stock information from https://www.alphavantage.co
company = 'Tesla'
alphavantage_parameters = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'apikey': alphavantage_apikey
}
alphavantage_api = f'https://www.alphavantage.co/query'
stock_response = requests.get(url=alphavantage_api, params=alphavantage_parameters)
stock_response.raise_for_status()
stock_info_dict: dict = stock_response.json()['Time Series (Daily)']
"""Example:
    {'2023-06-30': {
        '1. open': '260.6', 
        '2. high': '264.45', 
        '3. low': '259.89', 
        '4. close': '261.77', 
        '5. adjusted close': '261.77', 
        '6. volume': '112620784', 
        '7. dividend amount': '0.0000', 
        '8. split coefficient': '1.0'}, 
    '2023-06-29': {...}
...
}"""
# print(stock_info_dict)
latest_dates: list = list(stock_info_dict.keys())
"""['2023-06-30', '2023-06-29', ... ], starting from the latest available date in returned data"""
latest_close_price = float(stock_info_dict[latest_dates[0]]['4. close'])
second_latest_close_price = float(stock_info_dict[latest_dates[1]]['4. close'])
change_rate = abs(second_latest_close_price - latest_close_price) / latest_close_price
print('change rate: ', change_rate)


# ===NEWS REQUEST & SEND SMS===
new_catcher_url = "https://api.newscatcherapi.com/v2/search"
news_catcher_parameters = {
    "q": "Tesla",
    "lang": "en",
    "sort_by": "relevancy",
    "page": "1",
    'page_size': 5,
}
headers = {"x-api-key": NewsCatcher_apikey}
if change_rate >= 0.05:
    # get the first 5 news pieces for the COMPANY_NAME.
    newscatcher_response = requests.request("GET", new_catcher_url, headers=headers, params=news_catcher_parameters)
    """Request latest news on the company"""
    articles: list = newscatcher_response.json()['articles']
    titles = [article['title'] for article in articles]
    """Get only the titles of the news and saved in a list"""
    # Send a separate message with the percentage change and each article's title to your phone number.
    client = Client(twilio_account_sid, twilio_auth_token)
    change_rate = round((second_latest_close_price - latest_close_price) / latest_close_price, 3)
    direct_mark = '🔼' if change_rate >= 0 else '🔽'
    msg_str: str = f'TSLA {direct_mark}{change_rate}\n' \
                   f'Headline: 1. {titles[0]}; 2. {titles[1]}; 3. {titles[2]}'
    message = client.messages \
        .create(
            body=msg_str,
            from_='+447481337415',
            to='+447732234051'
    )
    print(message.status)



