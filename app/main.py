from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args) -> None:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            cache[args] = func(*args)
            return cache[args]
    return wrapper

    pass
