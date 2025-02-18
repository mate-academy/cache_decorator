from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        temp = (func.__name__, args, tuple(kwargs.items()))
        if temp in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[temp] = func(*args, **kwargs)

        return storage[temp]

    return inner
