from typing import Callable


def cache(func: Callable) -> Callable:
    data_cache = {}

    def wrapper(*args) -> Callable:
        if args in data_cache:
            print("Getting from cache")
        else:
            data_cache[args] = func(*args)
            print("Calculating new result")

        return data_cache[args]

    return wrapper
