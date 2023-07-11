# Scrape the 100 greatest movie recommendation data
# Write the results in a txt file.
# SKILLS: web scraping
# Difficulty: easy

import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'

response = requests.get(url=URL)
response.encoding = 'utf-8'
# print(response.encoding)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.findAll(name='h3', class_='title')
movies = [movie.getText() for movie in movies]
print(movies)
with open('movies.txt', 'w') as file:
    for movie in movies[::-1]:
        file.write(f'{movie}\n')
