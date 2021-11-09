import time
import requests
 
 
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print('Начало обёртки')
        func(*args, **kwargs)
        print('Конец обертки')
 
    return wrapper
 
 
def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        response = func(*args, **kwargs)
        finish = time.time()
        print(f'Время работы функции: {finish - start}')
        return response
    return wrapper
 
 
@benchmark
@decorator_function
def hello(name='world'):
    print(f'Hello, {name}')
 
 
@benchmark
def req(url='https://google.com/'):
    response = requests.get(url)
    return response.text
 
hello('Yan')
req()