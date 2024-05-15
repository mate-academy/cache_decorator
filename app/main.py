from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    result_cache = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        kwargs_str = str(kwargs)
        if (args, kwargs_str) in result_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_cache[(args, kwargs_str)] = func(*args, **kwargs)
        return result_cache[(args, kwargs_str)]

    return inner
