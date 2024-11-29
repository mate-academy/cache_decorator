from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args) -> Callable:
        if args in cache_data.keys():
            print("Getting from cache")
            return cache_data[args]

        cache_data[args] = func(*args)
        print("Calculating new result")
        return cache_data[args]

    return wrapper
