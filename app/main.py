from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        keys = (args, *kwargs.items())
        if keys in storage_cache:
            print("Getting from cache")
            return storage_cache[keys]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage_cache[keys] = result
        return result
    return wrapper
