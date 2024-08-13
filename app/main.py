from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_details = (args, tuple(kwargs.items()), func.__name__)

        if func_details in cache_dict:
            print("Getting from cache")
            return cache_dict[func_details]

        print("Calculating new result")
        func_result = func(*args, **kwargs)
        cache_dict[func_details] = func_result

        return func_result

    return wrapper
