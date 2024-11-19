import numpy as np
import time
from prettytable import PrettyTable

# Количество элементов в массиве
n = 1_000_000_000

# Количество экспериментов
experiments = 15

# Списки для хранения времени выполнения
time_int8_list = []
time_int16_list = []

# Проведение экспериментов
for _ in range(experiments):
    # Массив с np.int8 (изменен диапазон на 0-127)
    arr_int8 = np.random.randint(0, 128, size=n, dtype=np.int8)

    # Массив с np.int16
    arr_int16 = np.random.randint(0, 128, size=n, dtype=np.int16)

    # Измеряем время выполнения для np.int8
    start_time = time.time()
    result_int8 = arr_int8 + 10
    time_int8 = time.time() - start_time
    time_int8_list.append(time_int8)

    # Измеряем время выполнения для np.int16
    start_time = time.time()
    result_int16 = arr_int16 + 10
    time_int16 = time.time() - start_time
    time_int16_list.append(time_int16)

# Создание таблицы для вывода результатов
table = PrettyTable()
table.field_names = ["Эксперимент", "np.int8 (сек)", "np.int16 (сек)", "Разница (сек)", "Процентная разница (%)"]

# Заполнение таблицы данными
for i in range(experiments):
    difference = time_int16_list[i] - time_int8_list[i]
    percent_difference = (difference / time_int8_list[i]) * 100 if time_int8_list[i] != 0 else float('inf')
    table.add_row([i + 1, f"{time_int8_list[i]:.6f}", f"{time_int16_list[i]:.6f}", f"{difference:.6f}", f"{percent_difference:.2f}"])

print(table)

# Вычисление статистики
def calculate_statistics(times):
    return {
        'min': np.min(times),
        'sum': np.sum(times),
        'mean': np.mean(times),
        'std_dev': np.std(times),
        'max': np.max(times)
    }

stats_int8 = calculate_statistics(time_int8_list)
stats_int16 = calculate_statistics(time_int16_list)

# Вывод статистики
print("\nСтатистика для np.int8:")
print(f"Минимальное значение: {stats_int8['min']:.6f} секунд")
print(f"Сумма всех значений: {stats_int8['sum']:.6f} секунд")
print(f"Среднее значение: {stats_int8['mean']:.6f} секунд")
print(f"Стандартное отклонение: {stats_int8['std_dev']:.6f} секунд")
print(f"Максимальное значение: {stats_int8['max']:.6f} секунд")

print("\nСтатистика для np.int16:")
print(f"Минимальное значение: {stats_int16['min']:.6f} секунд")
print(f"Сумма всех значений: {stats_int16['sum']:.6f} секунд")
print(f"Среднее значение: {stats_int16['mean']:.6f} секунд")
print(f"Стандартное отклонение: {stats_int16['std_dev']:.6f} секунд")
print(f"Максимальное значение: {stats_int16['max']:.6f} секунд")
