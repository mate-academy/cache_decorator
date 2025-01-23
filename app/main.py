from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args) -> Callable:
        if args not in cached:
            print("Calculating new result")
            cached[args] = func(*args)
        else:
            print("Getting from cache")
        return cached[args]
    return inner
