n = int(input('Введите положительное число: '))

sum_ = n * (n + 1) // 2

# добавим int в вывод, чтобы число после деления не выводилось как float
print(f'Сумма первых {n} положительных чисел равна {sum_}')
