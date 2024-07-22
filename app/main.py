from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:

        key = (args, frozenset(kwargs.items()))

        if key in cache_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_results[key] = func(*args, **kwargs)

        return cache_results[key]

    return wrapper
