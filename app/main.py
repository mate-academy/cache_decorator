from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def inner(*args) -> tuple:
        inner_args = args
        if inner_args in dict_cache.keys():
            print("Getting from cache")
            return dict_cache[inner_args]
        print("Calculating new result")
        dict_cache[inner_args] = func(*args)
        return dict_cache[inner_args]
    return inner
