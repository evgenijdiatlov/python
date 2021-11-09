def is_negative(x):
    assert x > 0
 
 
def is_divided(x: int, y: int) -> bool:
    return x % y == 0
 
 
def is_odd(x):
    is_negative(x)
    return is_divided(x, 2)
 
 
def factorization(x):
    is_negative(x)
    result = [
        i for i in range(1, x+1)
        if is_divided(x, i)
    ]
    return result
 
 
def is_prime(x):
    is_negative(x)
    delimiters = factorization(x)
    return len(delimiters) == 2
    