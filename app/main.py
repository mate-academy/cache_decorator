from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args) -> int | str:
        if args in cache:
            print("Getting from cache")
            return cache.get(args)
        else:
            print("Calculating new result")
            cache[args] = func(*args)
            return cache[args]

    return wrapper
