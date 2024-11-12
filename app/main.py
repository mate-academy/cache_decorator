from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: list) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]
        else:
            result = func(*args)
            storage[args] = result
            print("Calculating new result")
            return result

    return wrapper
