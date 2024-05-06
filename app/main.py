from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_data[args] = result
            return result
    return inner
