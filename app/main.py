from typing import Callable


def cache(func: Callable) -> Callable:
    storage_cache = {}

    def wrapper(*args: int) -> int:
        if args in storage_cache:
            print("Getting from cache")
            return storage_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            storage_cache[args] = result
            return result
    return wrapper
