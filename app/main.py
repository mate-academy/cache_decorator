from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: int) -> int:
        if args not in cache_storage:
            cache_storage[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_storage[args]

    return wrapper
