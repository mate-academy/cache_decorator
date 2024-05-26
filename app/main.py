from typing import Callable


def cache(func: Callable) -> Callable:

    all_cache = {}

    def inner(*args) -> int:
        if args in all_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            all_cache[args] = func(*args)
        return all_cache[args]
    return inner
