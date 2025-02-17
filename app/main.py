from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args) -> Any:
        temp = tuple(args)
        if temp in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[temp] = func(*args)

        return storage[temp]

    return inner
