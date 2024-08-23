from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_storage = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[key] = func(*args, **kwargs)
        # one return in wrapper
        return cache_storage[key]

    return wrapper
