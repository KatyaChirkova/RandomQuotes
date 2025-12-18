import sys
import os

# Добавляем путь к backend для импорта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_quotes_file_exists():
    # Проверяем что файл с цитатами существует
    quotes_path = os.path.join("backend", "app", "quotes.json")
    assert os.path.exists(quotes_path), f"File {quotes_path} not found"

def test_quotes_valid_json():
    # Проверяем что JSON файл валиден
    import json
    quotes_path = os.path.join("backend", "app", "quotes.json")
    
    # Открываем и читаем файл
    with open(quotes_path, 'r', encoding='utf-8') as f:
        quotes = json.load(f)
    
    # Проверяем структуру
    assert isinstance(quotes, list), "Quotes should be a list"
    assert len(quotes) > 0, "Quotes list should not be empty"
    
    # Проверяем поля первой цитаты
    if quotes:
        assert "id" in quotes[0], "Quote should have 'id' field"
        assert "text" in quotes[0], "Quote should have 'text' field"
        assert "author" in quotes[0], "Quote should have 'author' field"

def test_backend_import():
    # Проверяем что backend модули импортируются
    try:
        from backend.app.database import load_quotes
        from backend.app.models import Quote
        # Если импорт успешен - тест проходит
        assert True
    except ImportError as e:
        # Если ошибка импорта - тест не проходит
        assert False, f"Import error: {e}"