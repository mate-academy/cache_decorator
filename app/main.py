from typing import Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args) -> Callable:

        if args in cache_store:
            print("Getting from cache")

            return cache_store[args]

        print("Calculating new result")

        result = func(*args)
        cache_store[args] = result

        return result
    return wrapper
