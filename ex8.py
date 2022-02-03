"""
8. Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""


def generate_characters(n: int, char: str):
    word = ""
    for i in range(n):
        word += char

    return word


def generate_characters_python_way(n: int, char: str):
    return char * n


if __name__ == '__main__':

    print(generate_characters(5, 'x'))
    print(generate_characters(10, 'pf*'))
    print(generate_characters_python_way(5, 'x'))
