from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        args += tuple(kwargs.values())
        if args not in cache_dict:
            cache_dict[args] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_dict[args]
        print("Getting from cache")
        return cache_dict[args]
    return inner
