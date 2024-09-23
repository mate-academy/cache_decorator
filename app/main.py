from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:

        cache_key = (func.__name__, args, tuple(kwargs.items()))

        if cache_key in cache_store:
            print("Getting from cache")
            return cache_store[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[cache_key] = result
        return result

    return inner
