from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        if any(isinstance(arg, (list, dict, set)) for arg in args):
            raise ValueError("All arguments must be immutable")
        key = (func, args, frozenset(kwargs.items()))

        if key in cache_storage.keys():
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper
