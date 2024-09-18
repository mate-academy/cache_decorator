from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    result_dict = {}

    @functools.wraps(func)
    def wrapper(*args) -> Any:
        key = args
        if key in result_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[key] = func(*args)
        return result_dict[args]

    return wrapper
