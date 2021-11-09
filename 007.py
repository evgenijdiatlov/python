import time
import requests
 
 
def decorator_function(func):
    def wrapper(*args, **kwargs):
        print('Начало обёртки')
        func(*args, **kwargs)
        print('Конец обертки')
 
    return wrapper
 
 
def benchmark(iterations):
    def actual(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iterations):
                response = func(*args, **kwargs)
            finish = time.time()
            print(f'Время работы функции: {(finish - start) / iterations}')
            return response
        return wrapper
    return actual
 
 
@benchmark
@decorator_function
def hello(name='world'):
    print(f'Hello, {name}')
 
 
@benchmark(iterations=10)
def req(url='https://google.com/'):
    print('KEK')
    response = requests.get(url)
    return response.text
 
hello('Yan')
req()