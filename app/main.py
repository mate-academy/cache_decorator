from typing import Callable


def cache(func: Callable) -> Callable:
    cache = {}

    def inner(*args, **kwargs) -> int:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache[args] = result
            return result
    return inner
