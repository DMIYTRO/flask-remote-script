# Flask Remote Script Runner

Веб-приложение на Flask для удаленного запуска Python-скриптов с отображением вывода в реальном времени.

## Функциональность

- Запуск Python-скриптов через веб-интерфейс
- Отображение вывода скрипта в реальном времени
- Поддержка WebSocket для мгновенной передачи данных
- Обработка ошибок и статусов выполнения
- Возможность доступа через ngrok

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш-username/flask-remote-script.git
cd flask-remote-script
```

2. Создайте виртуальное окружение и установите зависимости:
```bash
python -m venv .venv
source .venv/bin/activate  # для Linux/Mac
# или
.venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

3. Запустите приложение:
```bash
python app.py
```

4. Откройте в браузере: http://127.0.0.1:5000

## Технологии

- Flask
- Flask-SocketIO
- Python Threading
- WebSocket
- HTML/CSS/JavaScript 