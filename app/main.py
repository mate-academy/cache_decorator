from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = f"{args}, {kwargs}"
        if cache_key in cache_store:
            print("Getting from cache")
            return cache_store[cache_key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_store[cache_key] = result
        return result

    return wrapper
