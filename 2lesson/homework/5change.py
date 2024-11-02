#@title Решение

# валидация данных (решил не перегружать через try-except)
def get_valid_change():
    while True:
        change = input('Введите величину сдачи (в копейках): ')
        if change.isdigit():
            return int(change)

        print('Ошибка! Пожалуйста, введите целое число.')

# функция для получение словаря с кол-вом каждой монеты
def calculate(change):
    coin_denomination = [500, 200, 100, 50, 10, 5, 1]
    change_dict = {}

    for coin in coin_denomination:
        count = change // coin
        change_dict[coin] = count

        change -= count * coin

    return change_dict


def print_result(change_dict):
    print('\nДля выдачи сдачи потребуется:')
    print(f'{"Номинал":^9} | {"Кол-во":^9}')

    for key in change_dict:
        if key >= 100:
            info = f'{key // 100:<2} руб.'
        else:
            info = f'{key:<2} коп.'

        print(f'{info:<9} | {change_dict[key]:^9}')


change = get_valid_change()
change_dict = calculate(change)

print_result(change_dict)
