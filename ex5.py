"""
5. Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""


def inverted_string(some_string: str):

    inverted = str()

    for i in some_string[::-1]:
        inverted = inverted + i

    return inverted


if __name__ == '__main__':
    print(inverted_string("estoy probando"))
