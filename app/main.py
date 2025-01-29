
from typing import Callable
from functools import wraps

def cache(func: Callable) -> Callable:

    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper
