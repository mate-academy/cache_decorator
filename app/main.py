from typing import Callable


def cache(func: Callable) -> Callable:
    cache_values = {}

    def inner(*args) -> callable:
        if args in cache_values:
            print("Getting from cache")
            return cache_values[args]
        else:
            cache_values[args] = func(*args)
            print("Calculating new result")
            return cache_values[args]
    return inner
