from typing import Callable


def cache(func: Callable) -> Callable:
    data_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))
        if key in data_cache:
            print("Getting from cache")
            return data_cache[key]
        else:
            result = func(*args, **kwargs)
            data_cache[key] = result
            print("Calculating new result")
            return result
    return wrapper
