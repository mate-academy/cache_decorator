from typing import Callable


def cache(func: Callable) -> Callable:
    cache_value = {}

    def inner(*args, **kwargs):
        if str(args) in cache_value:
            print("Getting from cache")
            return cache_value[str(args)]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_value[str(args)] = result
            return result
    return inner
