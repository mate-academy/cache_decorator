from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_store = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> any:
        key = (*args, *kwargs.items())
        if key in cache_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
        return cache_store[key]
    return inner
