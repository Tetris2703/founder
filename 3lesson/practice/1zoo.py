"""
"импортируем таблицу" с 3-мя столбцами

левая граница | правая граница | цена билета
    0                 2             0

"""
AGE_RANGES = [
    (0, 2, 0),
    (3, 12, 140),
    (13, 65, 230),
    (66, float('inf'), 180)     # float('inf') - можно заменить на число
]

def calculate_ticket_price(age):
    for age_range in AGE_RANGES:
        # то ради чего это всё делалось =)
        lower_bound, upper_bound, price = age_range

        if lower_bound <= age <= upper_bound:
            return price

    return 0  # eсли возраст не попадает ни в один диапазон

# Основная функция (валидацию данных не стал выделять в отдельную функцию)
def main():
    total_price = 0

    while True:
        age_input = input("Введите возраст посетителя (пустая строка для окончания ввода): ")

        #
        if age_input == "":
            break

        try:
            age = int(age_input)
            ticket_price = calculate_ticket_price(age)
            total_price += ticket_price
        except ValueError:
            print("Пожалуйста, введите корректный возраст.")

    print(f"Сумма посещения зоопарка для этой группы составит {total_price:.2f} рублей")

# Точка входа
if __name__ == "__main__":
    main()
