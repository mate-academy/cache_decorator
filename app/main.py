import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_data = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (func.__name__, args, frozenset(kwargs.items()))
        if cache_key in stored_data:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_data[cache_key] = func(*args, **kwargs)

        return stored_data[cache_key]

    return wrapper
