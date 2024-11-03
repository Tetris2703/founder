"""
Для N все делители находятся в диапазон [2; sqrt(N)]
"""
from math import floor


def is_prime(num: int) -> bool:
    if num < 2:  # Числа меньше 2 не являются простыми
        return False

    upper_bound = floor(num ** 0.5)

    for divider in range(2, upper_bound + 1):
        if num % divider == 0:
            return False

    # Если ни одно из чисел не является делителем, то число простое
    return True


def main(n: int):
    for num in range(n):
        if num in (0, 1):
            print(f'{num:<2}  {"не простое не составное"}')
        elif is_prime(num):
            print(f'{num:<2}  {"простое"}')
        else:
            print(f'{num:<2}  {"составное"}')


if __name__ == '__main__':
    n = int(input("Введите число: "))
    main(n)
