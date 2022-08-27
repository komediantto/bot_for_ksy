# Telegram бот-счётчик *калорий* и **жиров**
![Python](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
## Описание
Имя моего бота @smoky_cal_bot. Бот считает *калории* и **жиры**: вы настраиваете свои собственные лимиты по жирам и калориям и в течение дня фиксируете сколько и чего съели. Бот запомнит ваши лимиты навсегда, достаточно внести их один раз по команде /settigs. Написал его для своей девушки, параллельно упражняясь с библиотекой aiogram. Итак, что он делает:
1. По команде старт приветствует пользователя и просит себя настроить
2. По команде /settings просит установить свои лимиты, сперва по калориям, затем по жирам.
3. При вводе сообщений по типу '20 калорий' или '30 жиров' - отнимает данную цифру из заданного лимита и выдаёт остаток по обоим пунктам
4. В 2 часа ночи обновляет лимиты. Теперь снова можно есть!
5. При выходе за рамки лимитов в течении дня - шлёт ободряющих пёсиков. ТОЛСТЫХ пёсиков.

## Инструкция для запуска
1. Склонируйте репозиторий на локальную машину и создайте в корне проекта текстовый файл '.env'.

2. Через [BotFather](https://t.me/BotFather) в Telegram создайте своего бота и получите его токен.

3. В файл '.env' запишите токен своего бота по такому типу
    ```python
    TOKEN = ваш токен
    ```
5. Создайте виртуальное окружение в корне проекта
    ```python
    python -m venv venv
    ```

4. Установите все зависимости из файла requirements.txt
    ```python
    pip install -r requirements.txt
    ```
    
5. Запустите файл main.py
    ```python
    python main.py
    ```
