from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        key = args

        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[key] = result
            return result

    return wrapper
