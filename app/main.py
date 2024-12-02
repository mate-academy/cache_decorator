from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cached = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in cached:
            print("Getting from cache")
            return cached[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached[key] = result
        return result

    return wrapper
