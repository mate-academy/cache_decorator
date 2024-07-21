from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[key] = result
        return result
    return wrapper
