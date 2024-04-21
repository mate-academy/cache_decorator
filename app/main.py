from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    dict_cache = {}

    @functools.wraps(func)
    def wraps(*args, **kwargs) -> Any:
        inner_args = (args, tuple(kwargs.items()))
        if inner_args in dict_cache.keys():
            print("Getting from cache")
            return dict_cache[inner_args]
        print("Calculating new result")
        dict_cache[inner_args] = func(*args, **kwargs)
        return dict_cache[inner_args]
    return wraps
