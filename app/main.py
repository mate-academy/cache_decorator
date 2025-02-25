from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs.items())))

        if key in dict_cache:
            print("Getting from cache")
            return dict_cache[key]

        value = func(*args, **kwargs)
        dict_cache[key] = value
        print("Calculating new result")

        return value

    return wrapper
