from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (func.__name__, args, frozenset(kwargs.items()))

        if cache_key in cache_data:
            print("Getting from cache")
            result = cache_data[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[cache_key] = result
        return result

    return wrapper
