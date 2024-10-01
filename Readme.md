# Telegram Bot для получения курса доллара

Этот бот позволяет узнать текущий курс доллара, используя данные с сайта Центрального банка России.

## Установка

1. Склонируйте репозиторий или скачайте файлы.
2. Установите зависимости:

```bash
pip install -r requirements.txt
```

3. В файле `config.py` укажите токен вашего тг-бота:
```python
TG_TOKEN="Ваш токен"
```

4. Запустите бота:
```bash
python main.py
```

## Использование бота

Напишите `/start` для начала общения.

Бот спросит ваше имя и выдаст текущий курс доллара.

## Зависимости

- Python 3.12.3
- pyTelegramBotAPI 4.23.0

- requests 2.32.3