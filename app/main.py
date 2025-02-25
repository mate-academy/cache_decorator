from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:

    cache_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if func not in cache_store:
            cache_store[func] = {}
        if key in cache_store[func]:
            print("Getting from cache")
            return cache_store[func][key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[func][key] = result
            return result
    return wrapper
