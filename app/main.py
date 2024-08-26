from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())), func.__name__)

        if cache_key not in cache_dict:
            print("Calculating new result")
            cache_dict[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_dict[cache_key]

    return wrapper
