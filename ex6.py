"""
6. Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

from ex5 import inverted_string


def is_palindrome(word: str):
    if word == inverted_string(word):
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_palindrome('radar'))
    print(is_palindrome('terepino'))
