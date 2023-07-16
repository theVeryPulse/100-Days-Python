# This program automatically plays the Cookie Clickers Game
# It checks for updates every 5 seconds and chooses the most expensive one that is affordable
# SKILLS: selenium, web scraping, website interaction
# Difficulty: medium

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(15)



FIVE_SECS = 5  # [seconds]
TIME_TO_STOP = 20
start = time.time()
timeout_start = time.time()



def to_number(src_num):
    """Transform a formatted number to int. E.g., 123,789: str to 123789: int"""
    if ',' in src_num:
        return int(''.join(src_num.split(',')))
    else:
        return int(src_num)


big_cookie = driver.find_element(By.ID, 'bigCookie')
print('Automation begins')
while True:
    if time.time() - timeout_start > FIVE_SECS:
        big_cookie = driver.find_element(By.ID, 'bigCookie')  # relocate the big cookie
        print('Checking available updates')
        cookies_num = to_number(driver.find_element(By.ID, 'cookies').text.split(' ')[0])
        print(f'Total cookies: {cookies_num}')
        item_to_buy = 0
        while True:
            product_price = to_number(driver.find_element(By.ID, f'productPrice{item_to_buy}').text)
            print(f'Checking product number {item_to_buy}')
            if product_price <= cookies_num:
                item_to_buy += 1
            else:
                driver.find_element(By.XPATH, f'//*[@id="product{item_to_buy-1}"]').click()
                # driver.find_element(By.ID, f'productPrice{item_to_buy-1}').click()
                print(f'Bought product number {item_to_buy-1}')
                break
        timeout_start = time.time()
    elif time.time() - start > TIME_TO_STOP:
        break
    else:
        big_cookie.click()
cookies_summary = driver.find_element(By.ID, 'cookies').text
print(f'Cookies summary: {cookies_summary}')