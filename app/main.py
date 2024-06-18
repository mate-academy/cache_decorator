from typing import Callable


def cache(func: Callable) -> Callable:
    cache_db = {}

    def wrapper(*args, **kwargs) -> any:
        general_args = (args, tuple(kwargs.values()))
        if general_args in cache_db:
            print("Getting from cache")
            return cache_db[general_args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_db[general_args] = result
            return result

    return wrapper
