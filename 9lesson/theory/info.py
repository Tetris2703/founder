import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression # Импортируем модель логистической регрессии


# Создаем набор данных

# Параметры медицинских карт
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])

y = np.array([0, 0, 0, 1, 1])

# Создаем модель логистической регрессии
model = LogisticRegression()

# Обучаем модель на наборе данных
model.fit(X, y)

# Получаем прогноз для нового наблюдения
new_observation = np.array([[6, 7]])
prediction = model.predict(new_observation)

# Выводим прогноз
print("Прогноз:", prediction)

# Получаем вероятности для каждого класса
probabilities = model.predict_proba(new_observation)

# Выводим вероятности
print("Вероятности:", probabilities)



# Создаем сетку значений
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1 # Вычислим минимальное и максимальное значение по оси Х
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1 # Вычислим минимальное и максимальное значение по оси У
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01), np.arange(y_min, y_max, 0.01)) # Строим сетку с шагом 0.01
Z = model.predict(np.c_[xx.ravel(), yy.ravel()]) # Делаем предсказание для каждой точки
# ravel() - вытягивает матрицу в 1-мерный массив
# np.c_ - метод объединения матриц
# np.c_[np.array([[1,2,3]]), np.array([[4,5,6]])] -> [[1 2 3 4 5 6]]

# Визуализируем границу принятия решений
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.8) # Рисуем контур
plt.scatter(X[:, 0], X[:, 1], c=y) # Рисуем точки до границы одним цветом, после другим

plt.xlabel('Основной симптом')
plt.ylabel('Сопутствующий симптом')
plt.xlim(xx.min(), xx.max())
plt.title('Логистическая регрессия')

plt.show()


