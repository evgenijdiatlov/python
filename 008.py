import time
import requests
 
 
FUNCTION_CALL_COUNT = {}
FUNCTION_CALL_TIME = {}
 
 
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        # func.__repr__()
        response = func(*args, **kwargs)
        finish = time.time()
        print(f'Время работы функции: {(finish - start)}')
        if FUNCTION_CALL_COUNT.get(func.__repr__()) is None:
            FUNCTION_CALL_COUNT.update({func.__repr__(): 0})
            FUNCTION_CALL_TIME.update({func.__repr__(): 0})
        FUNCTION_CALL_COUNT[func.__repr__()] += 1
        FUNCTION_CALL_TIME[func.__repr__()] += finish - start
        return response
    return wrapper
 
 
 
@benchmark
def req_google(url='https://google.com/'):
    response = requests.get(url)
    return response.text
 
 
@benchmark
def req_yandex(url='https://ya.ru/'):
    response = requests.get(url)
    return response.text
 
req_google()
req_yandex()
req_google()
req_yandex()
req_google()
req_yandex()
 
req_google()
req_yandex()
req_google()
req_yandex()
req_google()
req_yandex()
 
for key in FUNCTION_CALL_COUNT.keys():
    print(f'{key} avg: {FUNCTION_CALL_TIME[key] / FUNCTION_CALL_COUNT[key]}')
 