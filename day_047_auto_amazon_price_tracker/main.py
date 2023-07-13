# This program checks the price of an item on Amazon
# If the price is lower than preset expectation, it sends an email to notify the user
# SKILLS: web scraping, requests, smtplib
# Difficulty: easy

from notification_manager import NotificationManager
from bs4 import BeautifulSoup
import requests
import os

TARGET_PRICE = 100
# ===Get the page content===
url = 'https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
headers = {  # obtained from: https://myhttpheader.com/
    'User-Agent': os.getenv('user_agent'),
    'Accept-Language': 'en',
}
response = requests.get(url=url, headers=headers)
response.raise_for_status()
# print(response.text)

# ===Locate price info===
soup = BeautifulSoup(response.text, 'html.parser')
price_symbol = soup.find(name='span', class_='a-price-symbol').text
price_whole = soup.find(name='span', class_='a-price-whole').text
price_fraction = soup.find(name='span', class_='a-price-fraction').text
price: float = float(f'{price_whole}{price_fraction}')
print(f'Current price: {price_symbol}{price}')
# ===Send email if price is lower than target price===
if price <= TARGET_PRICE:
    print('Price is lower than target, sending email...')
    message = f'Your tracked item has hit your price target! Get it at: {url}'
    notification_manager = NotificationManager()
    notification_manager.send_emails(
        subject='An item is on sale!',
        text=message,
        to='philip_test_python@yahoo.com'
    )