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
        # return to twilio an accesible url (own server) to download content
        msg.media('http://mychrismartinez.tech/{:d}'.format(response))
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
    media = resources.files(n)
    return send_from_directory(directory='file_storage', path=str(media))


@app.route('/')
def welcome():
    """Landing page"""
    return "<h1 style='color:red'>Hola, Soy Michi!</h1>"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
