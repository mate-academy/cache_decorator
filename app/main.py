from typing import Callable


def cache(func: Callable) -> Callable:
    cached_values = {}

    def wrapper(*args) -> int:
        if args in cached_values:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            cached_values[args] = result
        return cached_values[args]

    return wrapper
