from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int | str:
        if args in cache:
            print("Getting from cache")
            return cache.get(args)
        else:
            print("Calculating new result")
            cache[args] = func(*args, **kwargs)
            return cache[args]

    return wrapper
