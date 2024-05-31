from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        # Checking for Immutability
        key = func.__name__, args, tuple(kwargs.items())
        if any(isinstance(arg, (list, dict, set)) for arg in args) or \
           any(isinstance(arg, (list, dict, set)) for arg in kwargs.values()):
            raise TypeError("All arguments must be immutable")

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        print("Calculating new result")
        cache_storage[key] = func(*args, **kwargs)
        return cache_storage[key]

    return inner
