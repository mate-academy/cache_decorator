from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args, *kwargs)
            return cache_dict[args]
        print("Getting from cache")
        return cache_dict[args]

    return wrapper
