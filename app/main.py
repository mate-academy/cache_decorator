from typing import Callable


def cache(func: Callable) -> Callable:
    cached_values = {}

    def wrapper(*args) -> int:
        if args in cached_values.keys():
            print("Getting from cache")
            return cached_values[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_values[args] = result
            return result

    return wrapper
