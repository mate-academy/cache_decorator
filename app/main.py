from functools import wraps
from typing import Callable
from typing import TypeVar

T = TypeVar("T")


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @wraps(func)
    def wrapper(*args) -> T:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_dict[args] = result
            return result

    return wrapper
