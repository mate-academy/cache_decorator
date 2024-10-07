from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]
    return wrapper
