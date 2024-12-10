from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args, **kwargs) -> Any:
        key = str(args) + str(kwargs)
        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            storage[key] = result
            return result
    return inner
