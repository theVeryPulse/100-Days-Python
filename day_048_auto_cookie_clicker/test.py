import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def to_number(src_num):
    if ',' in src_num:
        return int(''.join(src_num.split(',')))
    else:
        return int(src_num)


driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')

time.sleep(15)
product_unlocked = driver.find_element(By.ID, f'productPrice10')
print(type(product_unlocked.text), product_unlocked.text=='')

product_price = driver.find_element(By.ID, f'productPrice{0}')
product_price = int(''.join(product_price.text.split(',')))
print(product_price)

cookies_num = driver.find_element(By.ID, 'cookies')
cookies_num = cookies_num.text.split(' ')[0]
cookies_num = to_number(cookies_num)
print(cookies_num)