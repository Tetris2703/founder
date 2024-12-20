import numpy as np
import matplotlib.pyplot as plt

# Создаем нормализованные данные
mean = 0
std_dev = 1
num_samples = 1000

# Генерируем нормализованные данные
normalized_data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы нормализованных данных
plt.hist(normalized_data, bins=30, density=True, alpha=0.6, color='g')

# Добавляем линию нормального распределения
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = np.exp(-0.5 * ((x - mean) / std_dev) ** 2) / (std_dev * np.sqrt(2 * np.pi))
plt.plot(x, p, 'k', linewidth=2)

# Добавляем заголовок и метки осей
title = "Нормализованное распределение данных"
plt.title(title)
plt.xlabel('Значение')
plt.ylabel('Плотность')

# Отображаем график
plt.show()
