import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        arguments = f"{args}{kwargs}"
        if arguments in storage:
            print("Getting from cache")
            return storage[arguments]
        print("Calculating new result")
        result = func(*args, **kwargs)
        storage[arguments] = result
        return result
    return wrapper
