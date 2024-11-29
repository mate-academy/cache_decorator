from typing import Callable
import functools


def cache(func: Callable) -> Callable:

    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:

        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
            return result

    wrapper.cache = cache_dict
    return wrapper
