from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        arguments_key = f"{args}{kwargs}"
        if arguments_key in cache_dict:
            print("Getting from cache")
            return cache_dict.get(arguments_key)
        result = func(*args, **kwargs)
        cache_dict[arguments_key] = result
        print("Calculating new result")
        return result
    return wrapper
