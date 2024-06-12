from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    unique_values = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in unique_values:
            print("Getting from cache")
        else:
            print("Calculating new result")
            unique_values[key] = func(*args, **kwargs)
        return unique_values[key]
    return inner
