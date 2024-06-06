from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        keys = (args, *kwargs.items())

        if func not in storage_cache:
            storage_cache[func] = {}

        if keys in storage_cache[func]:
            print("Getting from cache")
            return storage_cache[func][keys]

        print("Calculating new result")
        result = func(*args, **kwargs)
        storage_cache[func][keys] = result
        return result
    return wrapper
