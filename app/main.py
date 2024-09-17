from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    catcher = {}

    @wraps(func)
    def wrapper(*args: Callable) -> Callable:
        if args in catcher:
            print("Getting from cache")
            return catcher[args]
        else:
            print("Calculating new result")
            result = func(*args)
            catcher[args] = result
            return result
    return wrapper
