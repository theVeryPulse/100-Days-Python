# Goal: scrap through data from a home-rent websites, autofill all data into Google Forms
# This can automate a simple data entry job
# SKILLS: web scraping, web interaction, OOP
# Difficulty: hard. Complicated task where many details require special attention,

import json
import random
import time
import requests
from bs4 import BeautifulSoup
from google_forms_fill import GoogleFormsHelper


class Property:
    """Record a home, attrs include address, monthly rent, and link to the home"""
    def __init__(self, address_of_building, monthly_rent, link):
        self.address = address_of_building
        self.monthly_rent = monthly_rent
        self.link = link


class DataEntryAutomation:
    def __init__(self):
        self.google_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSePSJMJdhb06v8_lVVZzyZCFzH2VSKam9smwsoFKCIo_cdMEQ/viewform?usp=sf_link'
        self.property_info_url = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'
        self.user_agents_list = [
            'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
            'rawUa: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82'
        ]
        self.headers = {
            'User-Agent': random.choice(self.user_agents_list),
            "Accept-Language": "en-US",
            'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
            'sec-ch-ua-platform': "Windows",
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
        }
        self.response = requests.get(url=self.property_info_url, headers=self.headers)
        self.response.raise_for_status()
        self.soup = BeautifulSoup(self.response.text, 'html.parser')
        # Get all prop names on a certain page
        self.page_data = self.soup.find(id='__NEXT_DATA__').text
        self.page_data_json: dict = json.loads(self.page_data)
        self.prop_list: list[Property] = []

    def get_data_from_current_page(self):
        """Gather all required information for properties from current page"""
        for item in self.page_data_json['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']:
            try:
                prop_address = item["address"]
                f'https://www.zillow.com{item["address"]}'
                price = item['units'][0]['price']
                if price is None:  # In case the home does not have ['units'][0]['price'] but directly ['price'] instead
                    price = item['price']
                # url = item['detailUrl']
                url = f'https://www.zillow.com{item["detailUrl"]}'
            except Exception as E:
                print(E)
            else:
                price = int(''.join(filter(str.isdigit, price)))  # Convert, e.g., "$2,725+" to 2725
                self.prop_list.append(
                    Property(
                        address_of_building=prop_address,
                        monthly_rent=price,
                        link=url
                    )
                )
            print(f'{self.prop_list[-1].address} | {self.prop_list[-1].monthly_rent} | {self.prop_list[-1].link}')
        """/props/pageProps/searchPageState/cat1/searchResults/listResults/0/buildingName"""

    def get_data_from_rest_pages(self):
        """Collect all data from the following pages"""
        next_page = 2
        while True:
            try:
                next_page_url = f'https://www.zillow.com/homes/for_rent/{next_page}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{next_page}%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.81167067480469%2C%22east%22%3A-122.05498732519531%2C%22south%22%3A37.47073410534477%2C%22north%22%3A38.07859933507607%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
                self.response = requests.get(url=next_page_url, headers=self.headers)
                self.soup = BeautifulSoup(self.response.text, 'html.parser')
                self.page_data = self.soup.find(id='__NEXT_DATA__').text
                self.page_data_json: dict = json.loads(self.page_data)
                self.get_data_from_current_page()
                next_page += 1
            except:
                break
            else:
                print(f'Page {next_page-1} content recorded')
                sleep_time = random.randint(50, 100) / 10
                time.sleep(sleep_time)

"""
Page examples:
https://www.zillow.com/homes/for_rent/2_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.81167067480469%2C%22east%22%3A-122.05498732519531%2C%22south%22%3A37.47073410534477%2C%22north%22%3A38.07859933507607%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D
https://www.zillow.com/homes/for_rent/3_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A3%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.81167067480469%2C%22east%22%3A-122.05498732519531%2C%22south%22%3A37.47073410534477%2C%22north%22%3A38.07859933507607%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D
page = 0
# Page pattern:
f'https://www.zillow.com/homes/for_rent/{page}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{page}%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.81167067480469%2C%22east%22%3A-122.05498732519531%2C%22south%22%3A37.47073410534477%2C%22north%22%3A38.07859933507607%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D'
"""


# === Main Program ===
data_entry_automation = DataEntryAutomation()
data_entry_automation.get_data_from_current_page()
for home in data_entry_automation.prop_list:
    # print(home.address, home.monthly_rent, home.link)
    print(home.monthly_rent)
# test.get_data_from_rest_pages()
with open('deleteme.txt', 'r') as f:
    for item in data_entry_automation.prop_list:
        f.write(item.address)
        f.write(item.monthly_rent)
        f.write(item.link)
input('Press enter to continue')

google_forms_helper = GoogleFormsHelper()
# google_forms_helper.sign_in()
google_forms_helper.fill_forms(data_entry_automation.prop_list)