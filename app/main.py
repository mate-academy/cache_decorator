from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cache_dict = {}

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        args += tuple(kwargs.values())
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_dict[args]
    return inner
