from typing import Callable
import functools


def cache(func: Callable) -> Callable:

    decorator_cache = {}

    @functools.wraps(func)
    def wrapper(*args) -> int:
        if args in decorator_cache:
            print("Getting from cache")
            return decorator_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            decorator_cache[args] = result
            return result
    return wrapper
