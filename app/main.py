from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args, **kwargs) -> any:
        key = (*args, *kwargs.items())
        if key in cache_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
            return cache_store[key]
        return cache_store[key]
    return inner
