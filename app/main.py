from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = args, frozenset(kwargs)
        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]
        else:
            print("Calculating new result")
            result = func(*args)
            result_dict[key] = result
            return result
    return wrapper
