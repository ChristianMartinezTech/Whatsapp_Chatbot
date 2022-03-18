import os
"""File Storing the responses to the user and also
files() method which includes the path for each resource"""

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
    """method to return the path of the media based on incoming code"""
    if code == 11:
        return('Resources/Grado_1/Espanol/Lenguaje_estudiante_1.pdf')
    if code == 12:
        return('Resources/Grado_1/Matematicas/Matematicas_estudiante_1.pdf')
    if code == 13:
        return('Resources/Grado_1/Ciencias_Naturales/CN_Fichas.pdf')
    if code == 14:
        return('Resources/Grado_1/Ciencias_Sociales/CS_Fichas.pdf')
    if code == 21:
        return('Resources/Grado_2/Espanol/Lenguaje_estudiante_2.pdf')
    if code == 22:
        return('Resources/Grado_2/Matematicas/Matematicas_estudiante_2.pdf')
    if code == 23:
        return('Resources/Grado_2/Ciencias_Naturales/CN_Grado02_01.pdf')
    if code == 24:
        return('Resources/Grado_2/Ciencias_Sociales/CS_Grado2_01.pdf')
    if code == 31:
        return('Resources/Grado_3/Espanol/Lenguaje_estudiante_3.pdf')
    if code == 32:
        return('Resources/Grado_3/Matematicas/Matematicas_estudiante_3.pdf')
    if code == 33:
        return('Resources/Grado_3/Ciencias_Naturales/CN_Grado03_01.pdf')
    if code == 34:
        return('Resources/Grado_3/Ciencias_Sociales/CS_Grado3_01.pdf')
    if code == 41:
        return('Resources/Grado_4/Espanol/LG_Grado04_01.pdf')
    if code == 42:
        return('Resources/Grado_4/Matematicas/MT_Grado04_01.pdf')
    if code == 43:
        return('Resources/Grado_4/Ciencias_Naturales/CN_Grado04_01.pdf')
    if code == 44:
        return('Resources/Grado_4/Ciencias_Sociales/CS_Grado4_01.pdf')
    if code == 51:
        return('Resources/Grado_5/Espanol/LG_Grado05_01.pdf')
    if code == 52:
        return('Resources/Grado_5/Matematicas/MT_Grado05_01.pdf')
    if code == 53:
        return('Resources/Grado_5/Ciencias_Naturales/CN_Grado05_03.pdf')
    if code == 54:
        return('Resources/Grado_5/Ciencias_Sociales/CS_Grado5_01.pdf')
