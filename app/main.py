from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        print("Calculating new result")
        cache_dict[key] = func(*args, **kwargs)
        return cache_dict[key]

    return inner
