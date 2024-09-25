from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> dict:
        key = (args, tuple(kwargs.items()))
        if key in cached_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_dict[key] = result
        return cached_dict[key]
    return inner
