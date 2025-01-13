from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    my_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        #nonlocal my_cache
        if my_cache.get((func.__name__, args)) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            my_cache[func.__name__, args] = result
            return result
        else:
            print("Getting from cache")
            return my_cache[func.__name__, args]
    return wrapper

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

long_time_func(1, 2, 3)
long_time_func(2, 2, 3)
long_time_func_2((5, 6, 7), 5)
long_time_func(1, 2, 3)
long_time_func_2((5, 6, 7), 10)
long_time_func_2((5, 6, 7), 10)