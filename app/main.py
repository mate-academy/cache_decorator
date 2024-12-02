from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:

    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:

        key = (args, tuple(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    return wrapper
