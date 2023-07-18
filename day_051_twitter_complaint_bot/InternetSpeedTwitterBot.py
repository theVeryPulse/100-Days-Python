import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        time.sleep(10)
        while True:
            try:
                accept = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
                accept.click()
            except:
                time.sleep(2)
            else:
                break
        # Click Go to begin test
        while True:
            try:
                print('Testing internet speed: ', end='')
                go = self.driver.find_element(By.XPATH,
                                              '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
                go.click()
            except:
                print('Failed. Retry later')
                time.sleep(2)
            else:
                print('Success')
                break
        time.sleep(20)
        # Find the data on page
        while True:
            try:
                print('Get download and upload speed: ', end='')
                download = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
                upload = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
                float(download.text)
                float(upload.text)
            except:
                print('Failed. Will retry in 5 seconds')
                time.sleep(5)
            else:
                print(f'Success. Download speed {download.text} Mbps. Upload speed {upload.text} Mbps')
                break
        self.down = float(download.text)
        self.up = float(upload.text)

    def tweet_at_provider(self, account, password, text='testing'):
        self.driver.get('https://twitter.com/home?lang=en')
        print('Initiate tweeting')
        # Input account
        while True:
            try:
                print('Input account: ', end='')
                email_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
                email_input.send_keys(account)
                next_step = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
                next_step.click()
            except:
                print('Failed')
                time.sleep(2)
            else:
                print('Success')
                break
        # Input password
        while True:
            try:
                print('Input password: ', end='')
                password_input = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
                password_input.clear()
                password_input.send_keys(password)
                login = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
                login.click()
            except:
                print('Failed')
                time.sleep(2)
            else:
                print('Success')
                break
        # Click tweet. Have to manually select text box to work (Perhaps due to Twitter's anti-bot efforts)
        while True:
            try:
                print('Sending tweet: ', end='')
                tweet_text = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
                # tweet.click()
                tweet_text.send_keys(text)
                tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]')
                tweet_button.click()
            except Exception as E:
                print('Failed')
                print(E)
                time.sleep(5)
            else:
                print('Success')
                break
