from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result

    return wrapper


@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)


@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list[int]:
    return [number ** power for number in n_tuple]
