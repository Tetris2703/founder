def sum_numbers() -> float:
    user_input = input("Введите число (или Enter для завершения): ")

    if user_input == "":
        return 0

    # предполагаем, что ввод корректный
    number = float(user_input)

    return number + sum_numbers()


# Точка входа
if __name__ == "__main__":
    total_sum = sum_numbers()
    print(f"Сумма введенных чисел: {total_sum}")
