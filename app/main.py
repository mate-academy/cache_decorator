from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper_cache(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        cache_value = func(*args, **kwargs)
        cache_dict[key] = cache_value

        return cache_value

    return wrapper_cache
