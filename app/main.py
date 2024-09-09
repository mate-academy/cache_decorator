from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_list = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        cache_key = (args, tuple(sorted(kwargs.items())), func.__name__,)

        if cache_key in cache_list:
            print("Getting from cache")
            result = cache_list[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_list[cache_key] = result
        return result

    return wrapper