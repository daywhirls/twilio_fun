import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

'''
 This starts a flask webserver on localhost:port5000 (default).

 We need to create an HTTP tunnel to this, so Twilio can reach the server.

 Using ngrok for this, it gives us a publicly addressible URL that we can paste into the "A Message Comes In" webhook in our Twilio web console.

 Don't forget to add /sms to the end of the route!
'''

# init Flask app
app = Flask(__name__)

# create /sms route for TWIML to understand
@app.route("/sms", methods=['GET','POST'])

def reply():
    resp = MessagingResponse() # init response object
    resp.message("What is up my dude? Twilio is awesome and I am happy.")
    return str(resp) # string representation of response

if __name__ == "__main__":
    app.run(debug=True)
