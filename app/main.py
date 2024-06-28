from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            result = func(*args, **kwargs)
            cache_store[args] = result
            print("Calculating new result")
        return result
    return inner
