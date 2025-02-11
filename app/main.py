from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_resullt = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print("Getting from cache")
            return cache_resullt[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_resullt[key] = result
        return result

    return wrapper
