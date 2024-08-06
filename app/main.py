from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_store = {}

    def inner(*args, **kwargs) -> Any:
        kwargs_tuple = tuple(sorted(kwargs.items()))
        key = (args, kwargs_tuple)
        if key in cache_store:
            print("Getting from cache")
            return cache_store[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_store[key] = result
            return result
    return inner
