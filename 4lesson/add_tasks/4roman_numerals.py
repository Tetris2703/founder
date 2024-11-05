def roman_to_decimal(roman):
    # Словарь для соответствия римских цифр и десятичных значений
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # Базовый случай: если строка пустая, возвращаем 0
    if not roman:
        return 0

    # Получаем значение первого символа
    first_value = roman_dict.get(roman[0], 0)

    # Если есть следующий символ, проверяем его значение
    if len(roman) > 1 and roman_dict.get(roman[1], 0) > first_value:
        # Если следующий символ больше, вычитаем первое значение
        return roman_to_decimal(roman[1:]) - first_value
    else:
        # В противном случае, добавляем первое значение
        return first_value + roman_to_decimal(roman[1:])


def assert_test():
    assert roman_to_decimal("II") == 2
    assert roman_to_decimal("CD") == 400
    assert roman_to_decimal("CM") == 900
    assert roman_to_decimal("MCMXCIV") == 1994
    assert roman_to_decimal("MMXXIII") == 2023

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    user_input = input("Введите римские цифры: ").upper()
    decimal_value = roman_to_decimal(user_input)

    print(f"Десятичное значение: {decimal_value}")

    assert_test()
