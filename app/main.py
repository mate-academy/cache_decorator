from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache:
            print("Getting from cache")
            return cache[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    return wrapper
