#### This app uses Flaskto respond to an incoming text to my twilio number
#### I have ngrok running in the background to point to my local host with a public url which i give to twilio


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from twilio.rest import Client

myTwilioPhone = '+12053786436'
myPhone = '+12056019915'
SID = 'AC50e703c81b0f481620791d6ae77140c1'
key = '3bae1713efdd12d1e340d7e0b65a067c'
#from red44botv3 import bot_stuff
#import xml


app = Flask(__name__)

@app.route("/sms",methods=['GET', 'POST'])
def response():
    client = Client(SID, key)
    message = client.messages.create(body = 'hello', from_=myTwilioPhone, to=myPhone)  # gets message to send from bot_stuff
    return(message.body)           #posts this on my local server which my ngrok app points too.  WEBHOOK twilioo

if __name__ == "__main__":
    app.run(debug=True)
