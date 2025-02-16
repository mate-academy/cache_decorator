from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    func.cache_dict = {}

    @wraps(func)
    def wrapper(*args: Callable, **kwargs: Callable) -> Callable:
        args_tuple = tuple(args)
        kwargs_tuple = tuple(sorted(kwargs.items()))
        cache_key = (args_tuple, kwargs_tuple)
        if cache_key in func.cache_dict:
            print("Getting from cache")
            return func.cache_dict[cache_key]
        print("Calculating new result")
        result = func(*args, **kwargs)
        func.cache_dict[cache_key] = result
        return result
    return wrapper
