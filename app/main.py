from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    res_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()), func.__name__,)
        if key in res_dict:
            print("Getting from cache")
            return res_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            res_dict[key] = result
            return result

    return wrapper
