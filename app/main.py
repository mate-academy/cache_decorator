from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    storage = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args in storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            storage[args] = func(*args)

        return storage[args]

    return inner
