from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        if (args, str(kwargs)) in cache_dict:
            print("Getting from cache")
            return cache_dict[(args, str(kwargs))]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[(args, str(kwargs))] = result
            return result
    return wrapper
