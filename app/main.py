from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args: tuple) -> int:
        if args in cache_dict:
            print("Getting from cache")
        else:
            cache_dict[args] = func(*args)
            print("Calculating new result")

        return cache_dict[args]

    return inner
