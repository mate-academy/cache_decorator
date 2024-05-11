from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args) -> tuple:
        key = args
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[key] = result
            return result

    return inner
