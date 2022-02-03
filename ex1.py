'''
1. Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. 
(Es cierto que python tiene una función max() incorporada, 
pero hacerla nosotros mismos es un muy buen ejercicio.
'''


def new_max(num_1: int, num_2: int):
    '''Takes two numbers and returns the maximum.

    Args:
        num_1(int): number
        num_2(int): number

    Returns:
        The maximum number between num_1 and num2
    '''

    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2
    elif num_1 == num_2:
        raise Exception('Values must not be equal')
    else:
        raise Exception('Something went wrong!')


if __name__ == '__main__':
    print(new_max(1, 2))
    print(new_max(3, 4))
    #print(new_max(5, 5))
