"""
клетка: а1

цифровой код символа ord('a') - 97 - нечетное

Если сумма цифрового кода буквы и цифры - четное, то клетка ЧЕРНАЯ
"""
# допустим, что координаты вводятся корректо
def cell_color(cell) -> str:
    char, num = cell

    if (ord(char) + int(num)) % 2 == 0:
        return 'чёрная'

    return 'белая'


if __name__ == '__main__':
    cell = input('Введите номер клетки: ')

    result = cell_color(cell)
    print(f'Цвет клетки {cell} - {result}')
