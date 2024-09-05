from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args) -> Callable:

        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        cache_dict[args] = func(*args)
        print("Calculating new result")
        return cache_dict[args]

    return wrapper
