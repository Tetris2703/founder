"""
По условию не требуется, но в идеале добавить вывод какие монеты требуются
"""


def can_make_change(amount: int,  num_coins: int, coins: list) -> bool:

    if amount == 0 and num_coins == 0:
        return True  # Сумма достигнута с нужным количеством монет
    if amount < 0 or num_coins <= 0:
        return False  # Либо сумма отрицательная, либо не осталось монет

    # Рекурсивно проверяем с каждой монетой
    for coin in coins:
        # Проверяем, можем ли составить сумму с использованием текущей монеты
        if can_make_change(amount - coin, num_coins - 1, coins):
            return True

    return False

def main():
    coins = [1, 5, 10, 25]

    amount = int(input("Введите сумму в центах: "))
    num_coins = int(input("Введите количество монет: "))


    if can_make_change(amount, num_coins, coins):
        print(f"Можно собрать сумму {amount} центов с помощью {num_coins} монет.")
    else:
        print(f"Нельзя собрать сумму {amount} центов с помощью {num_coins} монет.")

if __name__ == "__main__":
    main()
