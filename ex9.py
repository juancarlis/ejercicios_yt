"""
9. Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
    ****
    *********
    *******
"""

from ex8 import generate_characters


def procedure(arr: list):
    for elem in arr:
        print(generate_characters(elem, '*'))


if __name__ == '__main__':
    procedure([4, 9, 7])
