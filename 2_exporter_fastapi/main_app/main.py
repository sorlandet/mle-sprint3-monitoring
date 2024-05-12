import random
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from prometheus_fastapi_instrumentator import Instrumentator


# создание экземпляра FastAPI приложения
app = FastAPI()

# инициализируем и запускаем экпортёр метрик
Instrumentator().instrument(app).expose(app)

# обработка запросов к корове
@app.get("/predict")
def cow_answer(x: int, y: int):
    return {'prediction': x+y}
