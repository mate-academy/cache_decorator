from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result

    return wrapper
