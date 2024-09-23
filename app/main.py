from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__ ,args, frozenset(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            result = cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result
        return result
    return wrapper
