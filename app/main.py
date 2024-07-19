from typing import Callable
import functools
cache_dict = {}


def cache(func: Callable) -> Callable:
    global cache_dict

    @functools.wraps(func)
    def wrapper(*args) -> int:
        global cache_dict

        if args not in cache_dict[func.__name__]:
            cache_dict[func.__name__][args] = func(*args)
            print("Calculating new result")
            return cache_dict[func.__name__][args]

        else:
            print("Getting from cache")
            return cache_dict[func.__name__][args]

    cache_dict[func.__name__] = {}

    return wrapper
