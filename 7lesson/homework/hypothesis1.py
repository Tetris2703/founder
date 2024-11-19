import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from prettytable import PrettyTable

from scipy.stats import chisquare


# Отключим предупреждения Python, чтобы не захламлять лишним выводом наш Блокнот
import warnings
warnings.filterwarnings('ignore')

FILE_PATH = './the_movies_dataset/movies_metadata.csv'


# Шаг 1
df = pd.read_csv(FILE_PATH)

# Шаг 2
df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')

# Шаг 3
df['release_day'] = df['release_date'].dt.day_name()

# Шаг 4
release_counts = df['release_day'].value_counts()

# Шаг 5
total_count = release_counts.sum()
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
expected_counts = np.array([total_count / 7] * 7)

# Шаг 6
observed_counts = np.array([release_counts.get(day, 0) for day in days_of_week])

# Шаг 7
chi2_stat, p_value = chisquare(observed_counts, expected_counts)

# Шаг 8
table = PrettyTable()
table.field_names = ["День недели", "Наблюдаемые частоты", "Ожидаемые частоты"]

# Заполнение таблицы данными
for day, observed, expected in zip(days_of_week, observed_counts, expected_counts):
    table.add_row([day, observed, expected])

# Вывод таблицы
print(table)

# Шаг 9

alpha = 0.05  # Уровень значимости

# Создание таблицы
table = PrettyTable()

# Заголовки столбцов
table.field_names = ["Параметр", "Значение"]
table.add_row(["Уровень значимости (alpha)", alpha])
table.add_row(["p-value", p_value])

if p_value < alpha:
    conclusion1 = "Отвергаем нулевую гипотезу: распределение фильмов по дням недели отличается от равномерного."
else:
    conclusion1 = "Не отвергаем нулевую гипотезу: нет оснований считать, что распределение фильмов по дням недели отличается от равномерного."


print(table)

print("\nВыводы:")
print(conclusion1)

# Шаг 10: Визуализация результатов
plt.figure(figsize=(10, 6))
x = np.arange(len(days_of_week))  # Место для дней недели
width = 0.2  # Ширина столбцов

# Столбцы для наблюдаемых и ожидаемых частот
bars1 = plt.bar(x - width/2, observed_counts, width, label='Наблюдаемые частоты', color='blue')
bars2 = plt.bar(x + width/2, expected_counts, width, label='Ожидаемые частоты', color='orange')

# Добавление меток и заголовка
plt.xlabel('День недели')
plt.ylabel('Количество фильмов')
plt.title('Распределение фильмов по дням недели')
plt.xticks(x, days_of_week)
plt.legend()

# Показать график
plt.tight_layout()
plt.show()



