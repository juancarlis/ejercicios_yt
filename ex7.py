"""
7. Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
"""


def superposition(arr1: list, arr2: list):

    match = False

    for i in arr1:
        for j in arr2:
            if i == j:
                match = True

    return match


if __name__ == '__main__':
    print(superposition(['a', 'b', 'c', 'd'], ['d', 'e', 'f', 'g']))
    print(superposition(['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']))
