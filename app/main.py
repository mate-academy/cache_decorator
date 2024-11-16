from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        try:
            key = tuple(args)
        except TypeError as e:
            raise ValueError(f"All arguments must be hashable: {e}")

        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            result = func(*args)
            storage[key] = result
            return result

    return wrapper
