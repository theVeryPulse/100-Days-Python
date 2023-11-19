import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
GOOGLE_ACCOUNT = ''
GOOGLE_PASSWORD = ''


class Property:
    """Record a home, attrs include address, monthly rent, and link to the home"""
    def __init__(self, address_of_building, monthly_rent, link):
        self.address = address_of_building
        self.monthly_rent = monthly_rent
        self.link = link


class GoogleFormsHelper:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--lang=en')
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get('https://docs.google.com/forms/d/1Y02l2BxeFOkfQ-QnGT5CRJGZR3HzeWWtr3VVHQNhfSM/edit')

    def sign_in(self):
        """Autofill account and password and login, can be skipped if Google Forms are set not to require logging in"""
        sign_in = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div[3]/div[2]')
        sign_in.click()
        time.sleep(5)
        account = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input')
        account.send_keys(GOOGLE_ACCOUNT)
        next_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_button.click()
        password_input = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section[2]/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input')
        password_input.send_keys(GOOGLE_PASSWORD)
        next_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button')
        next_button.click()

    def fill_forms(self, property_list: list[Property]):
        for item in property_list:
            try:
                address_input = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
                price_input = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
                link_input = self.driver.find_element(By.XPATH, '/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
                address_input.send_keys(item.address)
                price_input.send_keys(item.monthly_rent)
                link_input.send_keys(item.link)
            except:
                print('retry in 2 seconds')
                time.sleep(2)
            else:
                submit = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
                submit.click()
                time.sleep(random.randint(70, 150)/10)  # Pause for a moment
                self.driver.get('https://docs.google.com/forms/d/1Y02l2BxeFOkfQ-QnGT5CRJGZR3HzeWWtr3VVHQNhfSM/edit')
                time.sleep(15)

""" 
# Test Code For GoogleFormsHelper.fill_forms()
prop1 = Property(1, 2, 3)
prop2 = Property(4, 5, 6)
test_list = [
    prop1,
    prop2,
]
google_forms_helper = GoogleFormsHelper()
google_forms_helper.fill_forms(test_list)
"""