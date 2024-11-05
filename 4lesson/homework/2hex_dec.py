def hex2int(hex_char):
    if hex_char in '0123456789ABCDEF':
        return int(hex_char, 16)
    else:
        raise "Ошибка: Неверный шестнадцатеричный символ."

def int2hex(decimal_num):
    if 0 <= decimal_num <= 15:
        return hex(decimal_num).upper()[2:]  # Убираем '0x' и приводим к верхнему регистру
    else:
        raise "Ошибка: Введите целое число от 0 до 15."


