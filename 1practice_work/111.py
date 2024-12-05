# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
#
# from prettytable import PrettyTable
#
# from scipy.stats import chisquare
#
#
# # Отключим предупреждения Python, чтобы не захламлять лишним выводом наш Блокнот
# import warnings
# warnings.filterwarnings('ignore')
#
# FILE_PATH = 'heart_disease_uci.csv'
#
#
# df = pd.read_csv(FILE_PATH)
# # print(df.head())
# #df.info()
#
# # Проверка на пропуски
# print(df.isnull().sum())
#
# # Обработка пропусков (можно удалить строки с пропусками или заполнить их)
# df = df.dropna(subset=['trestbps', 'chol', 'thalch', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])
#
# print(df.isnull().sum())
#
# # Преобразование столбца 'num' в категориальный (0 - отсутствие заболевания, 1 - наличие)
# df['num'] = df['num'].apply(lambda x: 1 if x > 0 else 0)
#
# # Анализ среднего возраста по наличию заболевания
# age_summary = df.groupby('num')['age'].mean().reset_index()
# print(age_summary)
#
# # Визуализация
# plt.figure(figsize=(8, 5))
# sns.barplot(x='num', y='age', data=age_summary)
# plt.xticks(ticks=[0, 1], labels=['Нет заболевания', 'Есть заболевание'])
# plt.title('Средний возраст по наличию сердечно-сосудистых заболеваний')
# plt.xlabel('Наличие сердечно-сосудистых заболеваний')
# plt.ylabel('Средний возраст')
# plt.show()

"""
На основе полученных данных о среднем возрасте для групп с сердечно-сосудистыми заболеваниями (num = 1) и без них (num = 0) можно сделать следующие выводы:

1. Средний возраст:

   • Для людей без сердечно-сосудистых заболеваний (num = 0) 
   средний возраст составляет примерно 52.6 года.

   • Для людей с сердечно-сосудистыми заболеваниями (num = 1) 
   средний возраст составляет примерно 56.7 года.

2. Сравнение:

   • Средний возраст людей с сердечно-сосудистыми заболеваниями на 4.04 года выше, 
   чем у людей без заболеваний. Это может указывать на то, что с увеличением возраста 
   действительно возрастает вероятность наличия сердечно-сосудистых заболеваний.

3. Вывод о гипотезе:

   • Полученные данные поддерживают гипотезу о том, что с увеличением возраста 
   увеличивается вероятность наличия сердечно-сосудистых заболеваний. Однако для 
   более глубокого анализа следует учитывать и другие факторы, такие как пол, 
   уровень физической активности, наличие других заболеваний и т.д.
"""

import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

# Загрузка данных
data = pd.read_csv('heart_disease_uci.csv')

# Проверка типов данных
print(data.dtypes)

# Преобразование всех столбцов в числовые, если это возможно
data = data.apply(pd.to_numeric, errors='coerce')

# Проверка на наличие пропущенных значений
print(data.isnull().sum())

# Заполнение пропусков только для числовых столбцов
data.fillna(data.select_dtypes(include=[np.number]).mean(), inplace=True)

# Проверка на наличие бесконечных значений
print(np.isinf(data).sum())

# Замена бесконечных значений на NaN и заполнение их средними значениями
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data.fillna(data.select_dtypes(include=[np.number]).mean(), inplace=True)

# Фильтрация данных на основе наличия сердечно-сосудистых заболеваний
group_0 = data[data['num'] == 0]['age']
group_1 = data[data['num'] == 1]['age']

# Выполнение t-теста
t_stat, p_value = stats.ttest_ind(group_0.dropna(), group_1.dropna(), equal_var=False)

print(f'T-Statistic: {t_stat}, P-Value: {p_value}')

# Интерпретация результатов t-теста
alpha = 0.05
if p_value < alpha:
    print("Существует статистически значимая разница в среднем возрасте между группами.")
else:
    print("Нет статистически значимой разницы в среднем возрасте между группами.")

# Преобразование категориальных переменных в числовые
data_encoded = pd.get_dummies(data, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal'], drop_first=True)

# Преобразование булевых значений в числовые
data_encoded = data_encoded.astype(float)

# Проверка типов данных после преобразования
print(data_encoded.dtypes)

# Определяем зависимую и независимые переменные
X = data_encoded.drop(columns=['num'])  # Удаляем зависимую переменную
y = data_encoded['num']

# Проверка на наличие пропущенных значений в X и y
print(X.isnull().sum())
print(y.isnull().sum())

# Проверка на наличие бесконечных значений в X и y
print(np.isinf(X).sum())
print(np.isinf(y).sum())

# Дополнительная проверка на наличие NaN и inf в X и y
if X.isnull().values.any() or np.isinf(X).values.any():
    print("X contains NaN or inf values.")
if y.isnull().values.any() or np.isinf(y).values.any():
    print("y contains NaN or inf values.")

# Добавляем константу для модели
X = sm.add_constant(X)

# Создаем модель логистической регрессии
model = sm.Logit(y, X)
result = model.fit()

# Выводим результаты модели
print(result.summary())






"""
T-тест:

T-Statistic: Показывает разницу между средними значениями возраста в двух группах.
P-Value: Если p-value меньше уровня значимости (обычно 0.05), это означает, что разница между средними значениями возраста в двух группах статистически значима.
Логистическая регрессия:

Коэффициенты: Показывают, как каждый фактор влияет на вероятность наличия сердечно-сосудистых заболеваний.
P-Value: Показывает статистическую значимость каждого коэффициента. Если p-value меньше 0.05, это означает, что фактор статистически значимо влияет на зависимую переменную.
"""


