from typing import Callable


def cache(func: Callable) -> Callable:
    cache_values = {}

    def inner(*args, **kwargs) -> callable:
        key = (func, args, tuple(kwargs.items()))
        if key in cache_values:
            print("Getting from cache")
        else:
            cache_values[key] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_values[key]
    return inner
