from typing import Callable, Any

cache_dict = {}


def cache(func: Callable) -> Callable:
    def inner(*args) -> Any:
        key = (func, args)
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args)
            return cache_dict[key]

    return inner
