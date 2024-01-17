from functools import wraps
from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any], **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            result = func(*args, **kwargs)
            cache_dict[key] = result
            print("Calculating new result")
            return result

    return wrapper
