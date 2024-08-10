from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args: tuple, **kwargs) -> Any:
        key = (func.__name__, *args, tuple(kwargs))

        if key in cache_dict.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)

        return cache_dict[key]

    return inner
