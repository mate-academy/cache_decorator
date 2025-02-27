from typing import Callable


def cache(func: Callable) -> Callable:
    store_cache = {}

    def wrapper(*args) -> int:
        if args in store_cache:
            print("Getting from cache")
            return store_cache[args]
        store_cache[args] = func(*args)
        print("Calculating new result")
        return store_cache[args]

    return wrapper
