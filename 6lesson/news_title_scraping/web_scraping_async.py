
# Вместо requests используем aiohttp, который позволяет выполнять асинхронные HTTP-запросы
import aiohttp
import asyncio
from bs4 import BeautifulSoup
from datetime import datetime


async def get_titles_from_page(session, url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    try:
        async with session.get(url, headers=headers) as response:
            html = await response.text()
    except Exception as e:
        print(f"Ошибка при запросе {url}: {e}")
        return []

    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.find_all('h3', class_='entry-title td-module-title')

    if not titles:
        print(f"Заголовки не найдены на странице {url}.")
        return []

    title_list = [title.find('a').text.strip() for title in titles]
    return title_list


async def get_scrap_file(titles):
    """Функция для записи заголовков в файл"""
    current_date = datetime.now().strftime("%d.%m.%y")
    filename = f"scrap{current_date}_async.txt"

    with open(filename, 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')

    print(f"Заголовки успешно сохранены в файл: {filename}")


async def main():
    base_url = "https://2051.vision/category/ii/page/"
    all_titles = []
    total_pages = 19

    # создаем единую сессию, которая используется для всех запросов
    async with aiohttp.ClientSession() as session:
        tasks = []
        for page in range(1, total_pages + 1):
            url = f"{base_url}{page}/"
            print(f"Извлечение заголовков с {url}...")
            tasks.append(get_titles_from_page(session, url))

        # Ждем завершения всех задач
        results = await asyncio.gather(*tasks)

        # Объединяем все заголовки
        for titles in results:
            all_titles.extend(titles)

    for title in all_titles:
        print(title)

    await get_scrap_file(all_titles)


if __name__ == "__main__":
    asyncio.run(main())
