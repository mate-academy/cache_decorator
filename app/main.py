from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result_cache = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in result_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_cache[key] =  func(*args, **kwargs)
        return result_cache.get(key)

    return inner
