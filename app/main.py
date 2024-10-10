from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached_results = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        if func.__name__ not in cached_results:
            cached_results[func.__name__] = {}
        if args in cached_results[func.__name__]:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_results[func.__name__][args] = func(*args)

        return cached_results[func.__name__][args]

    return inner
