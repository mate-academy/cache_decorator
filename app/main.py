from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = args + tuple(kwargs.items())
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            print("Calculating new result")
            return result
    return wrapper
