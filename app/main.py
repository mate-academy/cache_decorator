from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> int:
        key = (args, frozenset(kwargs.items()))
        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            storage[key] = res
            return res
    return wrapper
