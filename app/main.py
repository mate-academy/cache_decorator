from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache[args] = result
            return result
    return wrapper
