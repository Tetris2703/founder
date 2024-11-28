import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm # импортируем пакет для работы с методом опорных векторов

# Создаем набор данных

# Параметры медицинских карт
X = np.array([[1, 2], [3, 7], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 2, 0, 1, 1])

h = 0.01 # Шаг сетки
C = 1.0 # параметр регуляризации SVM
svc = svm.SVC(kernel='linear', C=1, gamma=0).fit(X, y) # здесь мы взяли линейный kernel (ядро)
# создаём сетку для построения графика
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

plt.subplot(1, 1, 1)
Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

result = plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.legend(result.legend_elements()[0], ['0', '1', '2'])
plt.xlabel('Основной симптом')
plt.ylabel('Сопутствующий симптом')
plt.xlim(xx.min(), xx.max())
plt.title('Метод опорных векторов с линейным ядром')
plt.show()