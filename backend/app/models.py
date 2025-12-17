from pydantic import BaseModel  # библиотека для проверки данных

class Quote(BaseModel):
    id: int
    text: str
    author: str
