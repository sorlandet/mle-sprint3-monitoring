import requests
import time

for i in range(30):
    params = {
        'x': str(i*10),
        'y': '-1000',
    }
    response = requests.get('http://localhost:1702/predict', params=params)
    time.sleep(5)