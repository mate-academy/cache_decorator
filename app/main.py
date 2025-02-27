from typing import Callable


def cache(func: Callable) -> Callable:
    store_cache = {}

    def wrapper(*args) -> int:
        if args not in store_cache:
            store_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return store_cache[args]

    return wrapper
