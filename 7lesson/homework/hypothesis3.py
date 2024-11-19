import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
import warnings

# Отключим предупреждения Python
warnings.filterwarnings('ignore')

# Загрузка данных
credits = pd.read_csv('./the_movies_dataset/credits.csv')
movies_metadata = pd.read_csv('./the_movies_dataset/movies_metadata.csv')

# Приводим столбец 'id' к строковому типу для обоих DataFrame

credits['id'] = credits['id'].astype(str)


# Объединим данные о фильмах с данными о касте
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


# Шаг 3: Определить известных актеров
threshold_votes = merged_data['vote_count'].quantile(0.999)
known_actors = merged_data[merged_data['vote_count'] > threshold_votes]['cast'].explode().unique()

# Создадим новый столбец, который будет указывать, есть ли известные актеры в касте
merged_data['has_known_actor'] = merged_data['cast'].apply(
    lambda x: any(actor in known_actors for actor in x) if isinstance(x, list) else False
)

# Шаг 4: Анализ данных
average_budget = merged_data.groupby('has_known_actor')['budget'].mean()



# Шаг 5: Визуализация результатов
plt.figure(figsize=(10, 6))  # Увеличиваем размер графика
plt.bar(['Без известных актеров', 'С известными актерами'], average_budget, color=['blue', 'orange'], width=0.4)  # Используем plt.bar для явного указания меток
plt.title('Средний бюджет фильмов с известными актерами и без')
plt.xlabel('Наличие известных актеров')
plt.ylabel('Средний бюджет')
plt.grid(axis='y')  # Добавляем сетку по оси Y для лучшей читаемости
plt.tight_layout()  # Автоматически подгоняем параметры графика
plt.show()

# Получаем средний бюджет для фильмов без известных актеров
average_budget_without_known_actors = average_budget.get(False, 'Нет данных')
average_budget_with_known_actors = average_budget.get(True, 'Нет данных')

# Выводим результаты
print(f"Средний бюджет фильмов без известных актеров: {average_budget_without_known_actors}")
print(f"Средний бюджет фильмов с известными актерами: {average_budget_with_known_actors}")
