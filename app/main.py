from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args) -> int | tuple:
        if args not in cache_data:
            print("Calculating new result")
            result = func(*args)
            cache_data[args] = result
            return cache_data[args]
        else:
            print("Getting from cache")
            return cache_data[args]

    return wrapper
