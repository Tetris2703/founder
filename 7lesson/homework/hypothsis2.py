import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Отключим предупреждения Python
import warnings
warnings.filterwarnings('ignore')

# Загрузка данных
movies_metadata = pd.read_csv('./the_movies_dataset/movies_metadata.csv')
credits = pd.read_csv('./the_movies_dataset/credits.csv')


# Приведение 'id' в credits к строковому типу
credits['id'] = credits['id'].astype(str)

# Проверка типов данных после изменения
print("Тип данных 'id' в movies_metadata:", movies_metadata['id'].dtype)
print("Тип данных 'id' в credits:", credits['id'].dtype)

# Объединение данных
merged_data = movies_metadata.merge(credits, left_on='id', right_on='id')



# Преобразуем бюджет и доходы в числовые значения
movies_metadata['revenue'] = pd.to_numeric(movies_metadata['revenue'], errors='coerce')
movies_metadata['budget'] = pd.to_numeric(movies_metadata['budget'], errors='coerce')

# Объединяем данные о фильмах с данными об актерах
credits['cast'] = credits['cast'].apply(eval)  # Преобразуем строку JSON в список
credits['cast'] = credits['cast'].apply(lambda x: [actor['name'] for actor in x])  # Извлекаем имена актеров
# Объединяем два датафрейма по идентификатору фильма
merged_data = movies_metadata.merge(credits, left_on='id', right_on='id')

# Убираем фильмы без дохода или бюджета
merged_data = merged_data[(merged_data['revenue'] > 0) & (merged_data['budget'] > 0)]


# Определяем пороги
thresholds = [0.999, 0.995, 0.99]
average_revenues = []

for threshold in thresholds:
    # Рассчитываем порог
    threshold_votes = merged_data['vote_count'].quantile(threshold)

    # Получаем список известных актеров
    known_actors = merged_data[merged_data['vote_count'] > threshold_votes]['cast'].explode().unique()

    # Фильтруем фильмы с известными актерами
    known_actors_movies = merged_data[merged_data['cast'].apply(lambda x: any(actor in known_actors for actor in x))]
    average_revenue_known_actors = known_actors_movies['revenue'].mean()

    # Фильтруем фильмы без известных актеров
    unknown_actors_movies = merged_data[~merged_data['cast'].apply(lambda x: any(actor in known_actors for actor in x))]
    average_revenue_unknown_actors = unknown_actors_movies['revenue'].mean()

    average_revenues.append((average_revenue_known_actors, average_revenue_unknown_actors))

# Преобразуем данные для графика
avg_revenue_known = [avg[0] for avg in average_revenues]
avg_revenue_unknown = [avg[1] for avg in average_revenues]

# Построение графиков
labels = ['99.9%', '99.5%', '99%']
x = range(len(labels))

plt.figure(figsize=(10, 6))

# Столбчатая диаграмма для известных актеров
plt.bar(x, avg_revenue_known, width=0.4, label='Известные актеры', color='blue', align='center')

# Столбчатая диаграмма для неизвестных актеров
plt.bar([p + 0.4 for p in x], avg_revenue_unknown, width=0.4, label='Неизвестные актеры', color='orange', align='center')

# Настройки графика
plt.xlabel('Порог голосов')
plt.ylabel('Средние кассовые сборы')
plt.title('Сравнение средних кассовых сборов фильмов')
plt.xticks([p + 0.2 for p in x], labels)
plt.legend()
plt.grid(axis='y')

# Показать график
plt.tight_layout()
plt.show()
