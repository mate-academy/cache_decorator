from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_data = {}

    @wraps(func)
    def wrapper(*args) -> Callable:
        if func.__name__ in cached_data:
            if args in cached_data[func.__name__]:
                print("Getting from cache")
                return cached_data[func.__name__][args]
        else:
            cached_data[func.__name__] = {}

        print("Calculating new result")
        cached_data[func.__name__][args] = func(*args)
        return cached_data[func.__name__][args]

    return wrapper
