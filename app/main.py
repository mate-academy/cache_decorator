import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
            return cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            if len(cached_results) >= 5:
                cached_results.popitem()
            cached_results[key] = result
            return result
    return wrapper
