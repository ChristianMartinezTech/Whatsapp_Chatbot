from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from models.base_module import MichiBot
import os
import requests

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    traffic = MichiBot()
    response = MichiBot(incoming_msg)

    responded = False
#    if 'quote' in incoming_msg:
#        # return a quote
#        r = requests.get('https://api.quotable.io/random')
#        if r.status_code == 200:
#            data = r.json()
#            quote = f'{data["content"]} ({data["author"]})'
#        else:
#            quote = 'I could not retrieve a quote at this time, sorry.'
#        msg.body(quote)
#        responded = True
    if type(response) is str:
        # return a cat pic
        msg.media()
        responded = True
    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()
