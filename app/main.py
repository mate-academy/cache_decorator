from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    former_functions = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items(),))
        if key in former_functions:
            print("Getting from cache")
            return former_functions[key]
        else:
            print("Calculating new result")
            former_functions[key] = func(*args, **kwargs)
            return former_functions[key]

    return wrapper
