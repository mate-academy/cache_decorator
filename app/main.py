from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def inner(*args: tuple) -> Any:
        nonlocal cache_dict
        if args in cache_dict.keys():
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args)
            return cache_dict[args]

    return inner
