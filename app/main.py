from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        cache_arg = (args, tuple(kwargs.items()))
        if cache_arg in func_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            func_cache[cache_arg] = func(*args, **kwargs)
        return func_cache[cache_arg]

    return wrapper
