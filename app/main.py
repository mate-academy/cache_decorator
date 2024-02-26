from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        key = args + tuple(kwargs.items())
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return wrapper
