from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> int:

        key = (args, frozenset(kwargs.items())) if kwargs else args

        if key in storage:
            print("Getting from cache")
            result = storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[key] = result

        return result

    return wrapper
