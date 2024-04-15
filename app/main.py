from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        arg_key = args
        if kwargs:
            arg_key += tuple(sorted(kwargs.items()))
        if arg_key not in cache_dict:
            print("Calculating new result")
            cache_dict[arg_key] = func(*args, **kwargs)
            return cache_dict[arg_key]
        print("Getting from cache")
        return cache_dict[arg_key]

    return wrapper
