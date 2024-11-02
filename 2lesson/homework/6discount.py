regular_price = 49.00
discount_rate = 0.60

quantity = int(input("Введите количество приобретенных вчерашних буханок хлеба: "))

discount_price = regular_price * (1 - discount_rate)
total_cost = discount_price * quantity

print(f"\nОбычная цена за буханку: {regular_price:5.2f} рублей")
print(f"Цена со скидкой: {discount_price:5.2f} рублей")
print(f"Общая стоимость: {total_cost:5.2f} рублей")
