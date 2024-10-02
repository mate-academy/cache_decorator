from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result
    return wrapper
