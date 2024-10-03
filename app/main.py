from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())), func.__name__)

        if key in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return wrapper
