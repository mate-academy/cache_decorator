from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args: Any) -> Callable:
        cache_key = (func.__name__, args)
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            # Calculate and store the result in the cache
            result = func(*args)
            cache_storage[cache_key] = result
            return result

    return wrapper
