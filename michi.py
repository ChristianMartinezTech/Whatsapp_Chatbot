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
        media = resources.files(response)
        msg.media(media)
        MichiBot.counter = 0
        MichiBot.book_code = ""
        responded = True
    if not responded:
        msg.body('Opción no valida')
    return str(resp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
