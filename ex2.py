"""
2. Definir una función max_de_tres(), que tome tres números como argumentos 
y devuelva el mayor de ellos.
"""


from ex1 import new_max


def max_of_three(n1: int, n2: int, n3: int):
    """Returns the maximum number between three given.

    Args:
        n1 (int): first number.
        n2 (int): second number.
        n3 (int): third number.

    Returns:
        int: maximum of the three given.

    """

    return new_max(new_max(n1, n2), n3)


if __name__ == '__main__':
    print(max_of_three(100, 200, 3))
