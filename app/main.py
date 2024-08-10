from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (func.__name__, *args, tuple(kwargs))

        if key in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[key] = func(*args, **kwargs)

        return storage[key]

    return inner
