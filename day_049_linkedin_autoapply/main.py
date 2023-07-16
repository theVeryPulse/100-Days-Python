# This program is supposed to automatically Easy Apply jobs on LinkedIn for you
# However, due to unknown issues, it cannot correctly click Easy Apply or Save button
# Skills: web scraping, web interaction, selenium
# Difficulty: medium

import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

print(
    os.environ.get('linkedin_username'),
    os.environ.get('linkedin_password')
)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
options.add_argument('--lang=en')
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3639735804&f_AL=true&keywords=python')

# Click Log in
while True:
    try:
        log_in = driver.find_element(By.XPATH, '/html/body/div[3]/header/nav/div/a[2]')
        log_in.click()
    except Exception as E:
        time.sleep(2)
        print(E)
    else:
        break
# Input login information
while True:
    try:
        username = driver.find_element(By.ID, 'username')
        password = driver.find_element(By.ID, 'password')
    except Exception as E:
        time.sleep(2)
        print(E)
    else:
        username.send_keys(os.environ.get('linkedin_username'))
        password.send_keys(os.environ.get('linkedin_password'))
        driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click()
        break
# Log in verification
input('Input anything to continue')
# Select 'software developer'
while True:
    try:
        select_job = driver.find_element(By.LINK_TEXT, 'Python Developer')
        select_job.click()
    except Exception as E:
        time.sleep(2)
        print(E)
    else:
        print('Job clicked')
        break
# Click 'easy apply' button
while True:
    try:
        # easy_apply = driver.find_element(By.LINK_TEXT, 'Easy Apply')
        easy_apply = driver.find_element(
            By.CLASS_NAME,
            'jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary'
        )
        easy_apply.click()
    except Exception as E:
        time.sleep(2)
        print(E)
    else:
        print('Easy apply clicked')
        break
# Click 'next' button
while True:
    try:
        next_button = driver.find_element(By.LINK_TEXT, 'Next')
        next_button.click()
    except Exception as E:
        time.sleep(2)
        print(E)
    else:
        break
# Click 'review' button
while True:
    try:
        review_button = driver.find_element(By.LINK_TEXT, 'Review')
        review_button.click()
    except Exception as E:
        time.sleep(2)
        print(E)
    else:
        break