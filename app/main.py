from functools import wraps
from typing import Callable

# Dictionary to store cached results for different functions
cached_results = {}

def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (func, args, tuple(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result
    return wrapper
