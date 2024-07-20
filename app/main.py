import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    stored_data = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in stored_data:
            print("Getting from cache")
            return stored_data[key]

        print("Calculating new result")
        stored_data[key] = func(*args, **kwargs)
        return stored_data[key]

    return wrapper
