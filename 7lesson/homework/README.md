## Задачи о гипотезах

В качестве обучающего датасета мы выбрали набор данных из 45000 фильмов, выпущенных в июле 2017 года или ранее. Данные включают актерский состав, съемочную группу, ключевые слова сюжета, бюджет, доходы, постеры, даты выхода, языки, производственные компании, страны, количество голосов на TMDB и средние значения голосов.

В этом наборе данных также есть файлы, содержащие 26 миллионов оценок от 270 000 пользователей для всех 45 000 фильмов. Оценки даны по шкале от 1 до 5 и были получены с официального веб-сайта GroupLens.

Этот набор данных состоит из следующих файлов:

- movies_metadata.csv. Основной файл метаданных фильмов. Содержит информацию о 45 000 фильмах, представленных в полном наборе данных MovieLens. Включает постеры, фоны, бюджет, доходы, даты выхода, языки, страны производства и компании.

- keywords.csv. Ключевые слова сюжета фильма. Доступно в виде строкового объекта JSON.

- credits.csv. Информация об актерах и съемочной группе для всех фильмов. Доступно в виде строкового объекта JSON.

- links.csv. Содержит идентификаторы TMDB и IMDB фильмов.

- links_small.csv. Содержит идентификаторы TMDB и IMDB небольшого подмножества из 9000 фильмов.

- ratings_small.csv. Подмножество из 100 000 оценок от 700 пользователей по 9000 фильмам.

### Гипотезы
Используя базу данных фильмов проверьте следующие гипотезы:
- Большинство фильмов выпускаются по пятницам
- Известные актеры снимаются в самых кассовых фильмах
- Известные актеры снимаются в самыx дорогих фильмах