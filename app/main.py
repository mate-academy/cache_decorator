from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key not in cache_storage:
            cache_storage[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_storage[key]

    return wrapper
