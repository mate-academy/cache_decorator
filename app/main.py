from typing import Callable, Any, Hashable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args: Hashable, **kwargs: Hashable) -> Any:
        cache_key = (args, tuple(kwargs.items()))
        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[cache_key] = result
        return result
    return inner
