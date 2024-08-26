from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_dict[args]

    return wrapper
