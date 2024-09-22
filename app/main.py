from typing import Callable
from functools import wraps

def cache(func: Callable) -> Callable:

    func_cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        func_cache[key] = result
        return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> int:
    return [number ** power for number in n_tuple]

