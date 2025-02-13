📓 Бот Заметок @stachievements_bot

Этот проект представляет собой Telegram-бот, который позволяет пользователям добавлять, просматривать и удалять текстовые заметки. Бот сохраняет заметки в текстовом файле и загружает их при каждом запуске.

▎🚀 Функции

- /start - Приветственное сообщение с инструкциями по использованию бота.
- /add <текст> - Добавить новую заметку.
- /view - Просмотреть все заметки.
- /delete <ID> - Удалить заметку по указанному ID.

🌟 /start
**Описание:** Приветственное сообщение, которое информирует пользователя о доступных командах и функциональности бота.
**Использование:** Просто введите /start в чат с ботом.

📝 /add 
**Описание:** Добавляет новую заметку с указанным текстом. Каждой заметке присваивается уникальный ID.

📜/view
**Описание:** Просматривает все сохраненные заметки. Бот отправляет список всех заметок с их уникальными ID.
**Использование:** Просто введите /view в чат с ботом.

❌### /delete <ID>
**Описание:** Удаляет заметку с указанным ID. После удаления бот подтверждает успешное удаление.

📝 Установка
1. Убедитесь, что у вас установлен Python 3.7 или выше. Вы можете скачать его с [официального сайта Python]
(https://www.python.org/downloads/).

2. Установите необходимые библиотеки:

bash
pip install python-telegram-bot
3. Скопируйте код бота в файл, например, bot.py.

4. Создайте файл note.txt в той же директории, где находится ваш скрипт. Этот файл будет использоваться для хранения заметок.

5. Замените TELEGRAM_TOKEN в коде на токен вашего бота. Вы можете получить токен, создав нового бота через [BotFather](https://t.me/botfather) в Telegram.

## Запуск

Запустите бота с помощью следующей команды:

bash
python bot.py

После запуска бот будет доступен в Telegram, и вы сможете взаимодействовать с ним через указанные команды.

## Примечания

- Заметки сохраняются в текстовом файле note.txt в формате ID - текст.
- Убедитесь, что у вас есть разрешения на запись в директорию, где находится ваш скрипт, чтобы бот мог создавать и изменять файл заметок.

## Разработка

Вы можете улучшить функциональность бота, добавив новые команды или изменив существующие. Например, можно реализовать возможность редактирования заметок или добавления меток к ним.


