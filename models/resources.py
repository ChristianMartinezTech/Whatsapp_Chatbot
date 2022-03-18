import os
"""File Storing the responses to the user"""
# First contact message
first_message = """Hola, soy Michi, tengo libros para ti.
¿Cuéntame en que grado estás?
1. 1° Primero
2. 2° Segundo
3. 3° Tercero
4. 4° Cuarto
5. 5° Quinto"""

# Choice option, we'll need to further develop this in the */base_module.py file
# choice = "Elegíste {}".format()

# User picking the subject
second_message = """¿Para qué asignatura buscas el libro?
1. Español/Lenguaje
2. Matemáticas
3. Ciencias Naturales
4. Ciencias Sociales
"""
def files(code):
    print("{:d} is in resources.files()".format(code))
    if code == 11:
        print("{:d} is the selected code".format(code))
        return('Resources/Grado_1/Espanol/Lenguaje_estudiante_1.pdf')
