from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args) -> Any:
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result
    return inner
