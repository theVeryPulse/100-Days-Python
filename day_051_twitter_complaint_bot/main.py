# This program tests your download and upload speed.
# If the speed is slower than what ISP promised, it will tweet a complaint
# Skills: web interaction, web scraping, selenium
# Difficulty: medium
import os
from InternetSpeedTwitterBot import InternetSpeedTwitterBot

TWITTER_ACCOUNT = os.getenv('twitter_account')
TWITTER_PASSWORD = os.getenv('twitter_password')
PROMISED_UP = 100  # Mpbs
PROMISED_DOWN = 100  # Mbps

internet_speed_twitter_bot = InternetSpeedTwitterBot()
internet_speed_twitter_bot.get_internet_speed()
if internet_speed_twitter_bot.up < PROMISED_UP or internet_speed_twitter_bot.down < PROMISED_DOWN:
    text = f'I was promised {PROMISED_DOWN}Mbps for download and {PROMISED_UP}Mbps for upload.' \
           f'But I am now only having {internet_speed_twitter_bot.down} and {internet_speed_twitter_bot.up}'
    internet_speed_twitter_bot.tweet_at_provider(account=TWITTER_ACCOUNT, password=TWITTER_PASSWORD, text=text)
