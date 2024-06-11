from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    unique_values = {}

    @wraps(func)
    def inner(*args) -> Callable:
        if args in unique_values:
            print("Getting from cache")
            return unique_values[args]
        else:
            print("Calculating new result")
            result = func(*args)
            unique_values[args] = result
            return result
    return inner
