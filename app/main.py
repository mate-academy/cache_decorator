import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(sorted(kwargs.items()))

        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[key] = result
            return result

    return wrapper
