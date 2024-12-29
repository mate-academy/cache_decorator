import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_history = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        cache_key = (args, tuple(kwargs.items()))

        if cache_key in cache_history:
            print("Getting from cache")
            return cache_history[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_history[cache_key] = result
        return result
    return wrapper
