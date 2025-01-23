from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args):
        if args not in cached.keys():
            cached[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
    return inner
