from typing import Any, Callable
import functools


def cache(func: Callable) -> Callable:
    dict_cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key not in dict_cache:
            dict_cache[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return dict_cache[key]

    return wrapper
