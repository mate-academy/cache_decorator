from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    runs = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        key = (args, frozenset(kwargs.items()), func.__name__,)
        if key in runs:
            print("Getting from cache")
        else:
            runs[key] = func(*args, **kwargs)
            print("Calculating new result")
        return runs[key]
    return wrapper
