# This program automatically follows all followers of a target account
# SKILLS: web interaction, web scraping, selenium
# Difficulty: medium (tricky to locate clickable button)

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

SIMILAR_ACCOUNT = 'taylorswift'
USERNAME = os.environ.get('account')
PASSWORD = os.environ.get('password')
print(USERNAME, PASSWORD)
# Open browser in English langauge
options = webdriver.ChromeOptions()
options.add_argument('--lang=en')
driver = webdriver.Chrome(options=options)
driver.get('https://www.instagram.com/')

# Cookies consent
while True:
    try:
        print('Cookies consent: ', end='')
        consent = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        consent.click()
    except Exception as E:
        time.sleep(2)
        print('Failed. Retry in 2 seconds')
    else:
        print('Success')
        break
time.sleep(5)
# Login
while True:
    try:
        print('Login: ', end='')
        account = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        login = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        account.clear()
        password.clear()
        account.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        login.click()
    except Exception as E:
        time.sleep(2)
        print('Failed. Retry in 2 seconds')
    else:
        print('Success')
        break
# Open followers page
time.sleep(10)
driver.get('https://www.instagram.com/taylorswift/followers/')
time.sleep(10)
# Follow all people displayed
i = 1
while True:
    try:
        follower = driver.find_element(By.XPATH, f'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button')
        follower.click()
    except Exception as E:
        print('Failed')
        print(E)
        break
    else:
        time.sleep(0.5)
        i += 1
        print('New user followed')
input('Press enter to continue')
