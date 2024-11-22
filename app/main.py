from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    results = dict({})

    @wraps(func)
    def wrapper(*args) -> callable:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            results[args] = result
            return result
    return wrapper
