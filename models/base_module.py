import os
from .resources import first_message, second_message
"""
Module base_module. Here are the Michibot Operations to return the rigth content
to user
"""


class MichiBot():
    """Class MichiBot"""
    counter = 0
    book_code = ""

    def __init__(self):
        MichiBot.counter += 1

    def bot_interaction(self, message):
        """"""
        if self.counter == 1:
            # method for 1st mesage
            if message is None:
                MichiBot.counter -= 1
                pass
            return first_message
        elif self.counter == 2:
            # method for 2nd message
            if len(message) == 1 and (ord(message) >= 49 and ord(message) <= 54):  # confirmar los números
                MichiBot.book_code += message
                return second_message  # definir jerarquía segun file_storage
            else:
                MichiBot.counter -= 1
                return first_message
        if self.counter == 3:
                # method for 3rd message
            if len(message) == 1 and (ord(message) >= 49 and ord(message) <= 54):
                MichiBot.book_code += message
                return int(MichiBot.book_code)
            else:
                MichiBot.counter -= 1
                return second_message
