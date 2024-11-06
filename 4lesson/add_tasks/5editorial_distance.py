def edit_distance(str1, str2):
    # базовые случаи
    if len(str1) == 0:
        return len(str2)  # eсли первая строка пустая, нужно добавить все символы второй строки
    if len(str2) == 0:
        return len(str1)  # eсли вторая строка пустая, нужно удалить все символы первой строки

    # eсли последние символы равны, продолжаем рекурсивно с оставшимися символами
    if str1[-1] == str2[-1]:
        return edit_distance(str1[:-1], str2[:-1])

    # eсли последние символы разные, рассматриваем все три операции
    insert_op = edit_distance(str1, str2[:-1])  # Вставка
    delete_op = edit_distance(str1[:-1], str2)  # Удаление
    replace_op = edit_distance(str1[:-1], str2[:-1])  # Замена

    # возвращаем минимальное количество операций + 1 для текущей операции
    return 1 + min(insert_op, delete_op, replace_op)

# Основная программа
if __name__ == "__main__":
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")

    distance = edit_distance(string1, string2)
    print(f"Редакционное расстояние между '{string1}' и '{string2}' равно {distance}.")
