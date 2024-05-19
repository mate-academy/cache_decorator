from typing import Callable


def cache(func: Callable) -> Callable:
    my_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        dict_key = (*args, tuple(kwargs.items()))

        if dict_key in my_cache:
            print("Getting from cache")
            return my_cache[dict_key]
        else:
            my_cache[dict_key] = func(*args, **kwargs)
            print("Calculating new result")
            return my_cache[dict_key]

    return wrapper
