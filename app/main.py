from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs), func.__name__)
        if key in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return inner
