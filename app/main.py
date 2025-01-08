from typing import Callable


def cache(func: Callable) -> Callable:
    my_cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        nonlocal my_cache
        if my_cache.get(args) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            my_cache[args] = result
            return result
        else:
            print("Getting from cache")
            return my_cache[args]
    return wrapper
