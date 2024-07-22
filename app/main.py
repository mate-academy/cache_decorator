from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:

    cache_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> None:

        if args in cache_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_results[args] = func(*args, **kwargs)

        return cache_results[args]

    return wrapper
