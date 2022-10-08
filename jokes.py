"""jokes script
"""
import json
import requests
import os
from twilio.rest import Client

url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url, timeout=10)
joke_dict = json.loads(response.text)
joke = joke_dict["value"]
print(joke)

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body=joke,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+919711026442'
                          )

print(message.sid)