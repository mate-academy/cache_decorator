from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:

    cache_storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        args += tuple(kwargs.values())
        if args not in cache_storage:
            print("Calculating new result")
            cache_storage[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_storage[args]
    return wrapper
