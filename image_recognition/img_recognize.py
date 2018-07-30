from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from tags import get_relevant_tags

app = Flask(__name__)

# create /sms route for TWIML to understand
@app.route("/sms", methods=['GET','POST'])

def sms_reply():
    resp = MessagingResponse()

    picList = []

    if request.form['NumMedia'] != 0: # if MM exists
        image_url = request.form['MediaUrl0'] # grabs first image in msg
        relevant_tags = get_relevant_tags(image_url)
        resp.message('\n'.join(relevant_tags))
    else:
        resp.message("Show me a picture. I want to learn!")
    return str(resp)

if __name__ == "__main__":
    app.run()
