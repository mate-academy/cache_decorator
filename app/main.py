from functools import wraps
from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        cache_key = (args, frozenset(kwargs.items()))

        if cache_key in cache_store:
            print("Getting from cache")
            return cache_store[cache_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[cache_key] = result
        return result

    return wrapper
