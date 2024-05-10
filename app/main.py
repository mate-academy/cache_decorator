from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs))
        if cache_key in cache_data:
            print("Getting from cache")
            return cache_data[cache_key]
        print("Calculating new result")
        cache_data[cache_key] = func(*args, **kwargs)
        return cache_data[cache_key]
    return inner
