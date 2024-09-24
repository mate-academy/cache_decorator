from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()), func.__name__)
        if key in cached:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached[key] = func(*args, **kwargs)
        return cached[key]

    return wrapper
