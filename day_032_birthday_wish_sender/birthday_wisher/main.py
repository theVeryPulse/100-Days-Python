# This program automatically sends birthday wishes to people who are having their birthdays
# It checks birthday information from './birthdays.csv'
# It randomly selects a template from './letter_templates' and replace '[NAME]' with the name of the birthday star
# SKILLS: pandas, SMTP, file i/o,
# Difficulty: medium

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import os
import random
import smtplib


# load birthday data
birthdays_dt = pd.read_csv('birthdays.csv')
print(birthdays_dt, type(birthdays_dt))
birthdays_dict_list = birthdays_dt.to_dict('records')
# note: each element is a dictionary corresponding to one person, e.g.:
# [{'name': 'Philip', 'email': 'philip.test.python@gmail.com', 'year': 1998, 'month': 2, 'day': 23}]

# record the date today
month_day_today = dt.datetime.today()
month_today = month_day_today.month
date_today = month_day_today.day
# check if anyone is having birthday today
birthday_star = {}
for person in birthdays_dict_list:
    if person['month'] == month_today and person['day'] == date_today:
        birthday_star = person
        print(f'{birthday_star["name"]} is having birthday today!')

# ===generate email===
# ---select a random template---
letter_filename = random.choice(os.listdir("./letter_templates"))
with open(f'./letter_templates/{letter_filename}', 'r') as file:
    content = file.read()
# ---replace name---
content = content.replace('[NAME]', f'{birthday_star["name"]}')
# ===send email===
# ---mail info---
# ####### PRIVATE INFO #######################
gmail_address = 'philip'
gmail_password = 'fffeb'
# ####### PRIVATE INFO #######################
# ---sending---
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.ehlo()
    connection.starttls()
    connection.login(user=gmail_address, password=gmail_password)
    connection.sendmail(
        from_addr=gmail_address,
        to_addrs=birthdays_dt['email'],
        msg=f'Subject:HAPPY BIRTHDAY!\n\n{content}'
    )
print('mail sent successfully')

