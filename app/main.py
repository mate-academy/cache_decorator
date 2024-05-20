from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_dict = {}

    def inner(*args: Any) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return cache_dict[args]
    return inner
