from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cache_store:
            print("Getting from cache")
        else:
            cache_store[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_store[args]
    return inner
