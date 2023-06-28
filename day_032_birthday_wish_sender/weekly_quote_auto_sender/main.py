# This program automatically sends emails to people from your contacts who are having birthday
# SKILLS: SMTP, datetime module,
# difficulty: easy
import smtplib
import datetime as dt
import random
# ####### PRIVATE INFO #######################
gmail_address = 'philip'
gmail_password = 'fffeb'
yahoo_address = 'philip'
# ####### PRIVATE INFO #######################
now = (dt.datetime.now())
print(now.year, type(now.year))
print(type(now))
birthdate = dt.datetime(year=1998, month=2, day=23)
print(f'birthdate {birthdate}')

weekday_today = dt.datetime.now().weekday()
print(f'today: {weekday_today} {type(weekday_today)}')

# load the quotes
with open('quotes.txt', 'r') as file:
    content = file.readlines()
quotes = [quote.replace('\n', '') for quote in content]
quote_to_send = random.choice(quotes)
print(quote_to_send)

# send the email
if weekday_today == 2:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.ehlo()
        connection.starttls()
        connection.login(user=gmail_address, password=gmail_password)
        connection.sendmail(
            from_addr=gmail_address,
            to_addrs=yahoo_address,
            msg=f'Subject:A quote for you\n\n{quote_to_send}'
        )
    print('mail sent successfully')