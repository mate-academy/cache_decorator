from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args) -> int:
        if args in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args)

        return cache_dict[args]

    return wrapper
