from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    result_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = args, frozenset(kwargs)
        if key in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[key] = func(*args)
        return result_dict[key]
    return wrapper
