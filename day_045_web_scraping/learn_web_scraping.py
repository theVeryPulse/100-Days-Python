# Scrape the latest article titles with the most upvote from ycominator
# SKILLS: web scraping
# Difficulty: easy

from bs4 import BeautifulSoup
import requests

response = requests.get(url='https://news.ycombinator.com/')
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())
first_title = soup.find(name='span', class_='titleline')
print('Title element:\n', first_title)

title_str = first_title.getText()
print('Title string:\n', title_str)

title_link = first_title.find(name='a').get('href')
print('Title link:\n', title_link)

title_upvote = soup.find(name='span', class_='score').getText()
print('Title upvote:\n', title_upvote)

title_link = []
all_titles = soup.findAll(name='span', class_='titleline')
for title in all_titles:
    string = title.getText()
    link = title.find(name='a').get('href')
    title_link.append([string, link])
print(title_link)
article_upvote = [score.getText() for score in soup.findAll(name='span', class_='score')]
print(article_upvote)
article_upvote_num = [int(score.split(' ')[0]) for score in article_upvote]
for i in range(len(title_link)):
    title_link[i].append(article_upvote_num[i])
title_link_upvote = title_link
print(title_link_upvote)

highest_vote = 0
article_highest_vote = []
for article in title_link_upvote:
    if highest_vote < article[2]:
        highest_vote = article[2]
        article_highest_vote = article
print(article_highest_vote)