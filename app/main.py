import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs))
        if key in result:
            print("Getting from cache")
            return result[key]

        result[key] = func(*args, **kwargs)
        print("Calculating new result")
        return result[key]

    return wrapper
