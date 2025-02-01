from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        if args in cache_dict:
            print("Getting from cache")
            return cache_dict[args]
        else:
            cache_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_dict[args]

    return inner
