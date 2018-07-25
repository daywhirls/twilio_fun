import os
from twilio.rest import Client

# Twilio credentials
TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH = os.environ["TWILIO_AUTH"]

# My personal phone number & twilio number
my_number = os.environ["MY_NUMBER"]
twilio_number = os.environ["TWILIO_NUMBER"]

client = Client(TWILIO_SID, TWILIO_AUTH)
client.messages.create(
    to=my_number,
    from_=twilio_number,
    body="Hello, world! This is my first ever Twilio App!"
)
