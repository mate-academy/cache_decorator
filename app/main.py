from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args: any, **kwargs: any) -> any:
        # Sort the keyword arguments
        kwargs_tuple = tuple(sorted(kwargs.items()))
        key = (args, kwargs_tuple)
        # Check if this key exists in the cache
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        # Calculate and store the result
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_storage[key] = result
        return result
    return wrapper
