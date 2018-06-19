#### This app uses Flaskto respond to an incoming text to my twilio number
#### I have ngrok running in the background to point to my local host with a public url which i give to twilio


from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from red44botv3 import bot_stuff
#import xml


app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'])
def response():
    message = bot_stuff()  # gets message to send from bot_stuff
    return(message)           #posts this on my local server which my ngrok app points too.  WEBHOOK twilioo

if __name__ == "__main__":
    app.run(debug=True)
