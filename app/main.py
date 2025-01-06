from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        func_name = func.__name__
        key_name = (args, frozenset(kwargs.values()))

        if func_name not in cache_dict:
            cache_dict[func_name] = {}
        if key_name not in cache_dict[func_name]:
            cache_dict[func_name][key_name] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_dict[func_name][key_name]
    return inner
