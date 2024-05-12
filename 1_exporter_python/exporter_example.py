from prometheus_client import start_http_server, Summary
import random
import time

#  Создаем метрику для отслеживания времени обработки запроса
REQUEST_TIME = Summary(
    'request_processing_seconds',
    'Time spent processing request',
    ['method', 'endpoint'])

# Используем функцию декоратор
@REQUEST_TIME.labels('GET', '/example').time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)

if __name__ == '__main__':
    
    # Запускаем сервер-экспортёр, который будет обрабатывать метрики
    # Для примера используем порт 8000
    start_http_server(8000)
    
    # Симулируем обработку запросов нашим приложением в бесконеном цикле
    while True:
        process_request(random.random())