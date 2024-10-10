from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key in cached_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[key] = func(*args, **kwargs)

        return cached_results[key]

    return inner
