from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[key] = func(*args, **kwargs)

        return cache_storage[key]

    return wrapper
