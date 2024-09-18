from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    result_dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs))
        if key in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[key] = func(*args, **kwargs)
        return result_dict[key]

    return wrapper
