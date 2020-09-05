from flask import Flask, request
import os
from twilio.rest import Client 
import json

app = Flask(__name__)

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

STATUSES = {
    "pre_transit":"is ready to go, but hasn't been shipped yet.",
    "in_transit":"is on it's way!",
    "out_for_delivery":"is out for delivery! It should be there soon!",
    "delivered":"has been delivered! Enjoy!"
}

@app.route('/', methods=['GET'])
def index():
    """
    Go to localhost:5000 to see a message
    """
    return ('This is a website.', 200, None)


@app.route('/events', methods=['POST'])
def events():
    # put webhook logic here
    data = json.loads(request.data)
    result = data['result']
    print(result['carrier'] + " - " + result['tracking_code'] + ": " + result['status'])
    if result['status'] in ["out_for_delivery","delivered"]:
        #send notification via Twilio
        human_readable = STATUSES[result['status']]
        message_body = "Your {0} package with tracking number, {1}, {2}".format(result['carrier'], result['tracking_code'], human_readable)
        message = client.messages.create(
            body=message_body,
            from_=os.environ.get('TWILIO_PHONE'),
             to=os.environ.get('NOTIFICATION_PHONE')
        )
        print(message.sid)

    print("Webhook Received")
    return '', 204


if __name__ == "__main__":
    app.run()
