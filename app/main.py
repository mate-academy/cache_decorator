from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Callable:

        if args in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[args] = func(*args)
        return cache_storage[args]

    return wrapper
