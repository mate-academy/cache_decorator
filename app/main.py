from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = args + tuple(kwargs.items())
        if key not in results:
            results[key] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results[args]
    return wrapper
