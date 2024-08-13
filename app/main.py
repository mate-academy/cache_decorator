from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        key = (args, kwargs_tuple, func.__name__,)
        if key in cache_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
        return cache_store[key]
    return wrapper
