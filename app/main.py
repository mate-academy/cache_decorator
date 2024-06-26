from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> str:
        key = (args, frozenset(kwargs.items()))

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        result = func(*args, **kwargs)
        cache_dict[key] = result
        print("Calculating new result")
        return result

    return wrapper
