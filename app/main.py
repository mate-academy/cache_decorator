from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    runs = {}
    name = None

    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        nonlocal name
        arguments = (args, frozenset(kwargs.items()))
        if arguments in runs and name == func.__name__:
            print("Getting from cache")
        else:
            name = func.__name__
            result = func(*args, **kwargs)
            runs[arguments] = result
            print("Calculating new result")
        return runs[arguments]

    return wrapper
