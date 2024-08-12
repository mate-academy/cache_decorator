from typing import Callable


def cache(func: Callable) -> Callable:
    cache_value = {}

    def inner(*args, **kwargs) -> (int, list):
        if args in cache_value.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_value[args] = func(*args, **kwargs)
        return cache_value[args]

    return inner
