from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args) -> str:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]

        cache_dict[args] = func(*args)
        print("Calculating new result")
        return cache_dict[args]

    return inner
