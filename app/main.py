from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = dict()

    @wraps(func)
    def cache_wrapper(*args, **kwargs) -> Any:
        cache_key = (args, frozenset(kwargs.items()), func.__name__,)

        if cache_key in cache_dict:
            print("Getting from cache")
            return cache_dict[cache_key]

        print("Calculating new result")
        cache_dict[cache_key] = func(*args, **kwargs)
        return cache_dict[cache_key]

    return cache_wrapper
