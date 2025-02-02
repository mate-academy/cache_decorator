from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args, **kwargs) -> int:

        key = (args, frozenset(kwargs.items())) if kwargs else args

        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[key] = result
            return result

    return wrapper
