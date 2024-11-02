"""
Считаю, что решение через множества - не сильно хорошее.
В маловероятной (но всё же ситуации), где случайно будут
браться одинаковые элементы -  мы потратим больше ресурсов,
чем могли бы
"""
from random import sample

def generate_lottery_numbers(count=6):

    # sample идеально подходит этой задаче
    lottery_numbers = sample(range(1, 50), count)
    lottery_numbers.sort()

    return lottery_numbers

def main():
    ticket_numbers = generate_lottery_numbers()
    print("Номера вашего лотерейного билета:", *ticket_numbers)

# Точка входа
if __name__ == "__main__":
    main()
