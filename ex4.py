"""
4. Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""


def sum_list(arr):
    total_sum = 0
    for elem in arr:
        total_sum = total_sum + elem

    return total_sum


def multip_list(arr):
    total_mult = 1
    for elem in arr:
        total_mult = total_mult * elem

    return total_mult


if __name__ == '__main__':
    print(sum_list([1, 2, 3, 4]))
    print(multip_list([1, 2, 3, 4]))
