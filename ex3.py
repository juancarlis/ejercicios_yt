"""
3. Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.
"""


def is_vowel(character: str):
    """ Returns True if argument is a vowel
    """

    vowels = ['a', 'e', 'i', 'o', 'u']

    character = character.lower()

    if character in vowels:
        return True
    else:
        return False


if __name__ == '__main__':
    print(is_vowel('A'))
    print(is_vowel('i'))
    print(is_vowel('X'))
