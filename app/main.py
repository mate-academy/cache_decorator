from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    my_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if my_cache.get((func.__name__, args)) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            my_cache[func.__name__, args] = result
            return result
        else:
            print("Getting from cache")
            return my_cache[func.__name__, args]
    return wrapper
