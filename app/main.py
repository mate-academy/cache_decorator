from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args) -> int:

        if args in result:
            print("Getting from cache")
        else:
            result[args] = func(*args)
            print("Calculating new result")
        return result[args]
    return wrapper
