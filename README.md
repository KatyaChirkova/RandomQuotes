# RandomQuotes - Генератор случайных цитат

Проект представляет собой веб-приложение для отображения случайных цитат. 
Backend реализован на Python с использованием FastAPI, frontend - на HTML/JavaScript.

## Установка и запуск
1. Установите зависимости: `cd backend && pip install -r requirements.txt`
2. Запустите сервер: `python -m uvicorn app.main:app --reload`
3. Откройте `frontend/purple.html` в браузере

## Функциональность
- Получение случайной цитаты через API endpoint `/random-quote`
- Простой веб-интерфейс для отображения цитат
- Автоматическая документация API доступна по `/docs`
- Unit-тесты для проверки корректности данных
- CI/CD pipeline на GitHub Actions

## Технологии
- Python, FastAPI, Pydantic
- HTML, CSS, JavaScript
- JSON для хранения данных
- pytest для тестирования
- GitHub Actions для CI/CD

## Разработчики
- Katya Chirkova - full-stack разработчик