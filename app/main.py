from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_data:
            print("Getting from cache")
            return cache_data[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[cache_key] = result
            return result

    return wrapper
