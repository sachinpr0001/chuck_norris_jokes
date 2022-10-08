from flask import Flask
import requests
import json
from twilio.rest import Client
import os

app = Flask(__name__)
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)


@app.route("/", methods=["GET", "POST"])
def bot():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url, timeout=10)
    joke_dict = json.loads(response.text)
    joke = joke_dict["value"]
    message = client.messages.create(
        body=joke,
        from_="whatsapp:+14155238886",
        to="whatsapp:ENTER YOUR MOBILE NUMBER HERE",
    )
    return message, 200


if __name__ == "__main__":
    app.run()
