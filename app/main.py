from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    d_cache = {}
    @wraps(func)
    def wrapper(*args: tuple) -> Callable:
        nonlocal d_cache
        if args in d_cache:
            print("Getting from cache")
            return d_cache[args]
        print("Calculating new result")
        res = func(*args)
        d_cache[args] = res
        return res

    return wrapper
