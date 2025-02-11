from typing import Callable
import functools

def cache(func: Callable) -> Callable:
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache:
            print("Getting from cache")
            return cache[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result

    return wrapper
