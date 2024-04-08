from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_box = {}   # Create dict

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        data = args + tuple(kwargs.items())
        if data not in cache_box:
            result = func(*args, **kwargs)
            cache_box[data] = result          # Added data that doesn't exist
            print("Calculating new result")
        else:
            result = cache_box[data]      # We take it from the kush
            print("Getting from cache")
        return result
    return wrapper
