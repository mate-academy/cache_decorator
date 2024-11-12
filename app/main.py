from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_args = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in cache_args:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_args[key] = func(*args, **kwargs)
        return cache_args[key]
    return wrapper
