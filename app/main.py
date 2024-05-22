from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    result_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        result_values = args + tuple(kwargs)
        if result_values in result_dict:
            print("Getting from cache")
            return result_dict[result_values]
        result_dict[result_values] = func(*args, **kwargs)
        print("Calculating new result")
        return result_dict[result_values]

    return wrapper
