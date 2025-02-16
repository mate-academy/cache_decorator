from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}
    def wrapper(*args):
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_dict[args]
    return wrapper
