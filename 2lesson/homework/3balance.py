rate = 0.04
balance = float(input("Введите сумму первоначального депозита: "))

balance_year1 = balance * (1 + rate)
balance_year2 = balance_year1 * (1 + rate)
balance_year3 = balance_year2 * (1 + rate)

# округляем уже после начиления процентов или нужно было округлять ПОСЛЕ каждого расчёта?
print(f'\nРасчет по сберегательному счёту на сумму {balance}')
print(f"- после 1-ого года: {round(balance_year1, 2):>10}")
print(f"- после 2-ого года: {round(balance_year2, 2):>10}")
print(f"- после 3-ого года: {round(balance_year3, 2):>10}")
