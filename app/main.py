from typing import Callable, Dict, Tuple
import functools


def cache(func: Callable) -> Callable:
    func_cache: Dict[Tuple, any] = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in func_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            func_cache[key] = func(*args, **kwargs)
        return func_cache[key]

    return wrapper
