from twilio.rest import Client
from log_in_information_private import *


class NotificationManager:
    """Send SMS through Twilio"""
    def __init__(self):
        self.client = Client(twilio_account_sid, twilio_auth_token)

    def send_msg(self, msg: str):
        """Send the input str as an SMS"""
        message = self.client.messages\
            .create(
                body=msg,
                from_='+447481337415',
                to='+447732234051'
        )
        print(message.status)