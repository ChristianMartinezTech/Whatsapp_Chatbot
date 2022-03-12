import os
"""Complete documentation!!!"""


class MichiBot():
    """"""
    counter = 0
    book_code = ""

    def __init__(self):
        MichiBot.counter += 1

    def bot_interaction(self, message):
        """"""
        if self.counter == 1:
            # method for 1st mesage
            if message is None:
                pass
            return str("""Hola, soy Michi, tengo libros para ti.\nCuéntame en que grado estás?
                       1. 1° Primaria
                       2. 2° Primaria
                       3. 3° Primaria
                       4. 4° Primaria
                       5. 5° Primaria""")  #definir jerarquía
        elif self.counter == 2:
            # method for 2nd message
            if len(message) == 1 and (ord(message) >= 48 and ord(message) <= 54):  # confirmar los números
                MichiBot.book_code += message
                return str("Ahora, para qué asignatura buscas el libro?\n1. Español/Lenguaje\n2. Matemáticas\n")  # definir jerarquía segun file_storage
            else:
                pass  # what to do if message is wrong
        if self.counter == 3:
                # method for 3rd message
            if len(message) == 1 and (ord(message) >= 48 and ord(message) <= 54):
                self.book_code = self.book_code + message
                return int(self.book_code)
