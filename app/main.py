from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def inner(*args) -> Any:
        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        print("Calculating new result")
        cache_data[args] = func(*args)
        return cache_data[args]
    return inner
