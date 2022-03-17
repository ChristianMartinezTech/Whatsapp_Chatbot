from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from models.base_module import MichiBot
from models import resources
import os
import requests

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    resp = MessagingResponse()
    msg = resp.message()
    traffic = MichiBot()
    response = traffic.bot_interaction(incoming_msg)
    responded = False
    if type(response) is str:
        # return menu options
        msg.body(response)
        responded = True
    if type(response) is int:
#        media = resources.files(response)
        msg.media('https://f8aa-201-221-176-11.ngrok.io/{:d}'.format(response))
        MichiBot.counter = 0
        MichiBot.book_code = ""
        responded = True
    if not responded:
        msg.body('Opción no valida')
    return str(resp)

@app.route('/<int:n>', strict_slashes=False)
def resource(n):
    media = resources.files(n)
    return media


if __name__ == '__main__':
    app.run()
