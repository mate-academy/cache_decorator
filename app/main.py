from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    arguments = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key_string = str(args) + str(kwargs)
        if key_string in arguments:
            print("Getting from cache")
            result = arguments[key_string]
        else:
            result = func(*args, **kwargs)
            arguments[key_string] = result
            print("Calculating new result")
        return result
    return wrapper
