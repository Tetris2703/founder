"""
Примечание:
Создание вложенной функции в данном случае позволяет инкапсулировать
логику рекурсии и избежать загрязнения глобального пространства имен
"""

def run_length_encoding(data):

    if not data:
        return []

    encoded = []
    current_char = data[0]
    count = 1

    # !вспомогательная рекурсивная функция для обработки данных
    def encode_helper(index):

        # переменные внешней области (неглобальной)
        nonlocal count, current_char

        if index >= len(data):
            # Добавляем последнюю серию в закодированный список
            encoded.extend([current_char, count])
            return

        if data[index] == current_char:
            count += 1
        else:
            # Записываем текущую серию и переходим к следующему символу
            encoded.extend([current_char, count])
            current_char = data[index]
            count = 1

        # Рекурсивный вызов для следующего индекса
        encode_helper(index + 1)

    # Начинаем с первого индекса
    encode_helper(1)

    return encoded


# Основная программа для демонстрации работы функции
if __name__ == "__main__":
    # Пример списка для кодирования
    example_list = ["A", "A", "A", "A", "A", "A", "A", "A",
                    "A", "A", "A", "A", "B", "B", "B", "B",
                    "A", "A", "A", "A", "A", "A", "B"]

    encoded_list = run_length_encoding(example_list)
    print("Закодированный список:", encoded_list)
