from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        if (func, args) in cache_dict:
            print("Getting from cache")
            return cache_dict[(func, args)]
        print("Calculating new result")
        cache_dict[(func, args)] = func(*args, **kwargs)
        return cache_dict[(func, args)]
    return inner
