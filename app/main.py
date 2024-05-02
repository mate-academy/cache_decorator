import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key not in cached_results:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cached_results[key]

    return wrapper
