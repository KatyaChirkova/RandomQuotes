from fastapi import FastAPI  # основной фреймворк для api
from fastapi.middleware.cors import CORSMiddleware  # для разрешения запросов из браузера
import random  # Для выбора случайной цитаты
from .database import load_quotes  # функция загрузки цитат
from .models import Quote  # модель данных

app = FastAPI(title="Random Quote Generator API")  # создание приложения

# настраиваем CORS - чтобы фронтенд в браузере мог обращаться к API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# загружаем цитаты
quotes = load_quotes()

# первый эндпоинт - главная страница (приветственное сообщение)
@app.get("/")
def read_root():
    return {"message": "Welcome to Random Quote Generator API"}

# второй эндпоинт - случайная цитата
@app.get("/random-quote", response_model=Quote)
def get_random_quote():

    return random.choice(quotes)  # возвращает случайную цитату