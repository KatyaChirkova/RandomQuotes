import json  # для работы с JSON файлами
import os  # для работы с путями файлов
from typing import List  # для указания типов данных
from .models import Quote  # импорт модели Quote из той же папки

def load_quotes() -> List[Quote]:
    # Загружает цитаты из JSON файла.
    file_path = os.path.join(os.path.dirname(__file__), "quotes.json")  # получение пути к файлу
    with open(file_path, "r", encoding="utf-8-sig") as file: # открытие и чтение файла
        data = json.load(file)
    return [Quote(**item) for item in data]  # конвертирует JSON-словари в Pydantic модели