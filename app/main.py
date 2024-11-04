from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def inner(*args: list) -> list:
        if args not in cached_results:
            cached_results[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cached_results[args]

    return inner
