# уменьшим название переменных, чтобы сократить громоздкость кода
small_b = int(input('Введите кол-во бутылок объемом <= 1 литр: '))
large_b = int(input('Введите кол-во бутылок объемом > 1 литра: '))

# множественное присваивание
small_b_cost, large_b_cost = 0.10, 0.25

# скобки для наглядности формулы
total = (small_b * small_b_cost) + (large_b * large_b_cost)

# f-строки
res = f'${total:.2f}'
print(f'Итоговая сумма {res}')
