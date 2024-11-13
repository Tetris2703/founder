"""
1. Ссылки с разными страница отличаются только номером
2. Заголовки находятся в h3 в классе entry-title td-module-title
3. Выгружаем и сохраняем в файл с текущей датой в названии
4. Добавляем статусы выгрузки в консоль для контроля процесса
"""


from bs4 import BeautifulSoup
import requests
from datetime import datetime


# Функция для извлечения заголовков новостей с указанной страницы
def get_titles_from_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    try:
        html = requests.get(url, headers=headers).content.decode('utf-8')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе {url}: {e}")
        return []

    soup = BeautifulSoup(html, 'html.parser')

    # Находим все заголовки новостей
    titles = soup.find_all('h3', class_='entry-title td-module-title')

    # Извлекаем текст заголовков
    title_list =  [title.find('a').text.strip() for title in titles]

    return title_list

#
def get_scrap_file(titles):
    """Функция для записи заголовков в файл"""

    current_date = datetime.now().strftime("%d.%m.%y")
    filename = f"scrap{current_date}.txt"

    # Записываем заголовки в файл
    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')  # Каждое название на новой строке

    print(f"Заголовки успешно сохранены в файл: {filename}")

def main():
    base_url = "https://2051.vision/category/ii/page/"
    all_titles = []

    total_pages = 19

    for page in range(1, total_pages + 1):
        url = f"{base_url}{page}/"
        print(f"Извлечение заголовков с {url}...")
        titles = get_titles_from_page(url)
        all_titles.extend(titles)  # Добавляем заголовки в общий список

    # Выводим все заголовки
    for title in all_titles:
        print(title)

    # Сохраняем заголовки в файл
    get_scrap_file(all_titles)

if __name__ == "__main__":
    main()
