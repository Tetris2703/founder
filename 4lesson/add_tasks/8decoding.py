"""
Примечание:
Создание вложенной функции в данном случае позволяет инкапсулировать
логику рекурсии и избежать загрязнения глобального пространства имен
"""

def decode(encoded_list):
    if not encoded_list:
        return []

    result = []

    # !вспомогательная рекурсивная функция для обработки данных
    def decode_helper(index):
        # не вышли ли мы за границы списка
        if index >= len(encoded_list):
            return

        # получаем текущий элемент и следующий (количество повторений)
        value = encoded_list[index]
        count = encoded_list[index + 1] if index + 1 < len(encoded_list) else 1

        result.extend([value] * count)

        # вызываем функцию для следующей пары
        decode_helper(index + 2)

    # запускаем с индексом 0
    decode_helper(0)

    return result


# Основная программа для демонстрации работы функции
if __name__ == "__main__":
    encoded_list = ["A", 12, "B", 4, "A", 6, "B", 1]
    decoded_list = decode(encoded_list)
    print("Закодированный список:", encoded_list)
    print("Расшифрованный список:", decoded_list)
