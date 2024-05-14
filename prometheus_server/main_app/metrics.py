from typing import Callable
from prometheus_fastapi_instrumentator.metrics import Info
from prometheus_client import Histogram
import logging

def main_app_predictions() -> Callable[[Info], None]:
    logging.error('Metric main_app_predictions initiated')
    METRIC = Histogram(
        "main_app_predictions",
        "Histogram of predictions",
        buckets=(1, 2, 4, 5, 10)
    )

    def instrumentation(info: Info) -> None:
        #res = await info.request.body()
        #logging.error(f'{dir(res)}')
        #logging.error(f'{res}')
        logging.error(f'{dir(info)}')
        logging.error(f'{info.request}')
        logging.error(f'{info.request.headers}')
        logging.error(f'{info.request.body()}')
        logging.error(f'{dir(info.response.body)}')
        logging.error(f'{info.response.body}')
        prediction = 2
        #prediction = float(info.response.json()['prediction'])
        METRIC.observe(prediction)
        
    return instrumentation
