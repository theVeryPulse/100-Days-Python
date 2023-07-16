import time

# SKILLS: web scraping, selenium

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = 'C:/Users/macpi/Desktop/Coding/chromedriver_win32/chromedriver.exe'


driver = webdriver.Chrome()

# ===Search by class name===
# driver.get('https://www.amazon.com')
# price = driver.find_element(By.CLASS_NAME, 'a-price')
# print(price.text)

# ===Search by XPATH===
# driver.get('https://www.python.org/')
# events = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
# event_time_dict: dict = {}
# for i in range(5):
#     event_time_dict[i] = {
#         'time': driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/time').text,
#         'name': driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i+1}]/a').text
#     }
# print(event_time_dict)
"""
//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time,
//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a

//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time
//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/a
"""

