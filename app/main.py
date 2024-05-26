from typing import Callable

cache_dict = {}


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> int:
        global cache_dict
        if (func, args) in cache_dict:
            print("Getting from cache")
            return cache_dict[(func, args)]
        else:
            print("Calculating new result")
            cache_dict[(func, args)] = func(*args, **kwargs)
            return cache_dict[(func, args)]
    return inner
