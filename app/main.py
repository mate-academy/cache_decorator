from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args) -> int:
        if not (args in cache_storage):
            cache_storage.update({args: func(*args)})
            print("Calculating new result")
            return cache_storage.get(args)
        else:
            print("Getting from cache")
            return cache_storage.get(args)

    return wrapper
