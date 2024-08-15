from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in cache_store:
            print("Getting from cache")
            result = cache_store[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[key] = result

        return result

    return wrapper
