from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args) -> int:
        if args in cache_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[args] = func(*args)

        return cache_data[args]

    return wrapper
