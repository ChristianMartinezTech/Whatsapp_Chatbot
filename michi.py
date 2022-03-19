from flask import Flask, request, send_file, send_from_directory
from twilio.twiml.messaging_response import MessagingResponse
from models.base_module import MichiBot
from models import resources
import os
import requests
"""Flask app to interact with the user trhough Twilio"""
app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    """Endpoint /bot
    & method to interpretate user incomming messages to generate a code url
    to retrieve the desired REA"""
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
        msg.media('https://7c3e-201-221-176-11.ngrok.io/{:d}'.format(response))
        MichiBot.counter = 0
        MichiBot.book_code = ""
        responded = True
    if not responded:
        msg.body('Opción no valida')
    return str(resp)

@app.route('/<int:n>', strict_slashes=False)
def resource(n):
    """Endpoint /<int:n>. Method resource useful to return the right file
    based on the incoming code(int)"""
    print("incoming code:", n)
    media = resources.files(n)
    print(media)
    return send_from_directory(directory='file_storage', path=str(media))

if __name__ == '__main__':
    app.run()
