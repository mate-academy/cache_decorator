from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[args] = result
            return result
    return wrapper
