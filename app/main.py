from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (func.__name__, args, frozenset(kwargs.items()))

        if key not in storage:
            print("Calculating new result")
            storage[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return storage[key]

    return wrapper
