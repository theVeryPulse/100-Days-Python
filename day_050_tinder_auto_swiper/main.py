# Tinder Auto Swipe
# This programs automatically logs in through Facebook and swipes people for you
# SKILLS: web interaction, selenium
# Difficulty: medium

import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://tinder.com/')
# Click login
while True:
    try:
        login = driver.find_element(
            By.XPATH,
            '//*[@id="t1951895747"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
        )
        login.click()
    except:
        time.sleep(2)
    else:
        print('Login clicked')
        break
# Click login with Facebook
while True:
    try:
        login_fb = driver.find_element(
            By.XPATH,
            '//*[@id="t223514671"]/main/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button'
        )
        login_fb.click()
    except:
        time.sleep(2)
    else:
        print('Login clicked')
        break
# Switch to popup window
base_window = driver.window_handles[0]
while True:
    try:
        fb_login_window = driver.window_handles[1]
        driver.switch_to.window(fb_login_window)
        print('Switch to window ->', driver.title, end=': ')
    except:
        print('failed')
        time.sleep(2)
    else:
        print('success')
        break
# Click cookies consent
while True:
    try:
        print('Trying clicking consent: ', end='')
        consent = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div/div/div[4]/button[2]')
        consent.click()
    except Exception as E:
        print('failed')
        print(E)
        time.sleep(2)
    else:
        print('success')
        break
# Fill in login information
while True:
    try:
        print('Trying filling in login information: ', end='')
        username = driver.find_element(By.ID, 'email')
        username.send_keys(os.environ.get('username'))
        password = driver.find_element(By.ID, 'pass')
        password.send_keys(os.environ.get('password'))
        login = driver.find_element(By.NAME, 'login')
        login.click()
    except:
        print('failed')
        time.sleep(2)
    else:
        print('success')
        break
# Begin swiping
input('Press enter to continue')
for i in range(50):
    try:
        print('Swiping: ', end='')
        left_swipe = driver.find_element(
            By.XPATH,
            '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button'
        )
    except Exception as E:
        print('failed')
        print(E)
        time.sleep(2)
    else:
        print('success')
