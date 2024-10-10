from typing import Callable, Any
import functools


def cache(func: Callable) -> Any:
    data_server = {}

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key in data_server:
            print("Getting from cache")
            return data_server[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            data_server[key] = result
            return result

    return wrapper
