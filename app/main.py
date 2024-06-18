from typing import Callable


def cache(func: Callable) -> Callable:
    cache_db = {}

    def wrapper(*args) -> any:
        if args in cache_db:
            print("Getting from cache")
            return cache_db[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_db[args] = result
            return result

    return wrapper
