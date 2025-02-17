from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    data_cache = {}

    @wraps(func)
    def wrapper(*args) -> int:
        if args in data_cache:
            print("Getting from cache")
            return data_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            data_cache[args] = result
            return result

    return wrapper
