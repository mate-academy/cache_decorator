from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_list = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())), func.__name__,)

        if cache_key in cache_list:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_list[cache_key] = func(*args, **kwargs)
        return cache_list[cache_key]

    return wrapper
