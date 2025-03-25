# Telegram Bot для списка литературы

Этот проект представляет собой бота для Telegram, который извлекает список литературы с указанного веб-ресурса и предоставляет пользователю возможность вывести список всех источников или случайный источник из данного списка.

Бот использует библиотеку `telebot` для взаимодействия с Telegram API, а также библиотеки `requests` и `BeautifulSoup` для извлечения данных с веб-страницы. Пользователи могут использовать команды для вывода списка источников или получения случайного источника.

### Команды бота:
- `/start`: приветственное сообщение с подсказками.
- `/list`: выводит полный список источников.
- `/random`: выводит случайный источник из списка.

## Запуск кода

1. **Скачайте или скопируйте код:** 
Скачайте код проекта со страницы GitHub или создайте новый файл для бота.

2. **Установите нужные библиотеки:**
Для работы с этим ботом необходимо установить несколько библиотек Python. Используйте команду ниже для установки библиотек:
pip install -r requirements.txt

3. **Настройка Telegram API токена:**
- Для работы бота вам нужно создать бота в Telegram и получить токен с помощью [BotFather](https://core.telegram.org/bots#botfather).
- Вставьте ваш токен в строку TOKEN = 'YOUR_BOT_TOKEN' в коде.

4. **Запуск бота:**
python telegram_literature_bot.py

После этого бот будет работать и реагировать на команды, отправленные пользователями в Telegram.

## Структура кода

- find_resources(): функция для извлечения списка литературы с веб-страницы. Считывает все заголовки и ищет раздел "Литература".
- start_message(): обработка команды /start, выводит приветственное сообщение и предлагает доступные команды.
- list_currencies(): обработка команды /list, выводит все источники литературы.
- random_resources(): обработка команды /random, выводит случайный источник из списка.
- Веб-страница для извлечения данных: https://znanierussia.ru/articles/Лингвистика

## Примечания

- Код использует библиотеку BeautifulSoup для парсинга HTML, извлекая данные с веб-страницы.
- Убедитесь, что веб-страница доступна, иначе бот не сможет извлечь источники.
- Бот реализует простое меню с кнопками для выбора команды /list или /random.
