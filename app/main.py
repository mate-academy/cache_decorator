from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (func, args, tuple(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper
