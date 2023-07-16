from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# driver.get('https://en.wikipedia.org/wiki/Main_Page')
# Find element by XPATH and click it
"""
article_sum = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(article_sum.text)
article_sum.click()
"""
# Find element by the text
"""
talk = driver.find_element(By.LINK_TEXT, 'Talk')
talk.click()
"""
# Input and enter
"""
search = driver.find_element(By.NAME, 'search')
search.send_keys('Python')
"""
#
driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element(By.NAME, 'fName')
last_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
sign_up = driver.find_element(By.TAG_NAME, 'button')

first_name.send_keys('123')
last_name.send_keys('123')
email.send_keys('123@123.com')
sign_up.click()

input("Press enter to exit;")