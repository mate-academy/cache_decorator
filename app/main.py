from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def inner(*args, **kwargs) -> tuple:
        key = (args, tuple(kwargs.items()))
        if key in cache_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
        return cache_store[key]
    return inner
