from typing import Callable
from functools import wraps

def cache(func: Callable):
    """Decorator to cache results of function calls with immutable arguments."""
    cache_storage = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        print("Calculating new result")
        result = func(*args)
        cache_storage[args] = result
        return result

    return wrapper  # Return the wrapper function, not a function call!

@cache
def long_time_func(a: int, b: int, c: int) -> int:
    return (a ** b ** c) % (a * c)

@cache
def long_time_func_2(n_tuple: tuple, power: int) -> list:
    return [number ** power for number in n_tuple]
