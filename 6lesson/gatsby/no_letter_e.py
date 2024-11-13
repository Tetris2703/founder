import string
import matplotlib.pyplot as plt
from collections import defaultdict
from typing import Dict


def get_percent_dict(sym_count_dict: Dict[str, int]) -> Dict[str, float]:
    """Получаем процентную статистику всех букв в тексте"""

    percent_dict = {}

    # Сумма всех символов
    total_sym = sum(value for value in sym_count_dict.values())

    for letter, count in sym_count_dict.items():
        if total_sym > 0:
            percent_dict[letter] = (count / total_sym) * 100
        else:
            percent_dict[letter] = 0

    return percent_dict


def get_stats(sym_count_dict: Dict[str, float]) -> None:
    """Выводит статистику по буквам."""

    rarest_letter = min(string.ascii_lowercase, key=lambda x: sym_count_dict.get(x, 0))

    print("Статистика по буквам:")
    for letter in string.ascii_lowercase:
        print(f"{letter}: {sym_count_dict.get(letter, 0):.2f}%")

    print(f"\nБуква, которая встречалась реже всего: '{rarest_letter}' {sym_count_dict.get(rarest_letter, 0)} раз")

    # Построение столбчатой диаграммы
    letters = list(string.ascii_lowercase)  # Убедитесь, что буквы в алфавитном порядке
    percentages = [sym_count_dict.get(letter, 0) for letter in letters]

    plt.figure(figsize=(10, 6))

    # Определяем цвета столбцов
    colors = ['#6287a2' if percent > 6 else '#5ec0ca' for percent in percentages]

    bars = plt.bar(letters, percentages, color=colors)

    # Подписи осей
    plt.xlabel('Буквы', fontsize=14)
    plt.ylabel('Процент (%)', fontsize=14)

    # Заголовок графика
    plt.title('Статистика по буквам в тексте', fontsize=16)

    # Подпись каждого столбца с уменьшенным шрифтом
    for i in range(len(letters)):
        plt.text(i, percentages[i] + 0.5, f'{percentages[i]:.2f}%', ha='center', fontsize=8)

    # Добавление сетки для наглядности
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Добавление легенды
    green_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#5ec0ca', markersize=10, label='< 6%')
    blue_patch = plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#6287a2', markersize=10, label='> 6%')
    plt.legend(handles=[green_patch, blue_patch], loc='upper right')

    # Увеличение верхней границы графика
    plt.ylim(0, max(percentages) + 2)  # Увеличиваем верхнюю границу на 10%

    # Показать график
    plt.show()


def main(file_name: str) -> None:
    """Основная функция для чтения файла и подсчета статистики по буквам."""

    sym_count_dict = defaultdict(int)

    # Читаем файл и собираем статистику
    with open(file_name, 'r') as file:
        for line in file:
            # Убираем знаки препинания и переводим в нижний регистр
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()
            for char in line:
                if char in string.ascii_lowercase:  # Проверяем, является ли символ буквой
                    sym_count_dict[char] += 1

    percent_dict = get_percent_dict(sym_count_dict)

    get_stats(percent_dict)


if __name__ == '__main__':
    file_name = 'gatsby.txt'
    main(file_name)
