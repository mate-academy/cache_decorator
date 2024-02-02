from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    def inner(*args) -> None:
        if args not in cache_dict:
            cache_dict[args] = func(*args)
            print("Calculating new result")
            return cache_dict[args]
        print("Getting from cache")
        return cache_dict[args]

    return inner
