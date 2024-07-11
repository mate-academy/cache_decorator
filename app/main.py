from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args, **kwargs) -> Callable:
        if func not in cache_store:
            cache_store[func] = {}

        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_store[func]:
            print("Getting from cache")
            return cache_store[func][cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[func][cache_key] = result
            return result

    return wrapper
