from typing import Callable


def cache(func: Callable) -> Callable:
    cache_value = {}

    def inner(*args, **kwargs) -> (int, list):
        if args in cache_value:
            print("Getting from cache")
            return cache_value[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_value[args] = result

    return inner
