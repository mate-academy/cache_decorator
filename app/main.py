from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_kwargs = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        checked_kwargs = tuple(kwargs.items())
        checked = (args, checked_kwargs)
        if checked in stored_kwargs:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_kwargs[checked] = func(*args, **kwargs)
        return stored_kwargs[checked]

    return wrapper
