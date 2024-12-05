from typing import Callable


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache_data:
            print("Getting from cache")
            return cache_data[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_data[key] = result
        return result

    return wrapper

