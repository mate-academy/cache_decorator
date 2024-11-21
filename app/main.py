from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        if isinstance(args, (str, int, float, tuple, bool)):
            if args in cache_storage:
                print("Getting from cache")
                return cache_storage[args]
            else:
                print("Calculating new result")
                result = func(*args)
                cache_storage[args] = result
                return result
        else:
            print("Not immutable data")
    return wrapper
