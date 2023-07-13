import smtplib
from email_account_info_private import gmail_address, gmail_password
from twilio.rest import Client
from log_in_information_private import *


class NotificationManager:
    """Functions:
    - Send SMS through Twilio
    - Send email through Gmail"""
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)
        self.gmail_address = gmail_address
        self.gmail_password = gmail_password

    def send_msg(self, msg: str):
        """Send the input str as an SMS"""
        message = self.client.messages\
            .create(
                body=msg,
                from_='+447481337415',
                to='+447732234051'
        )
        print(message.status)

    def send_emails(self, subject: str, text: str, to: str):
        """Send a single letter to target address"""
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(user=self.gmail_address, password=self.gmail_password)
            try:
                connection.sendmail(
                    from_addr=self.gmail_address,
                    to_addrs=to,
                    msg=f'Subject: {subject}\n\n{text}'
                )
            except Exception as E:
                print(f'Error: {E}')
            else:
                print(f'mail sent successfully sent to {to}')