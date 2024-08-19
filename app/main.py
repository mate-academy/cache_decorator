from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_list = {}

    def inner(*args, **kwargs) -> Any:
        if args not in cache_list:
            cache_list[args or kwargs] = func(*args, **kwargs)
            print("Calculating new result")
            return cache_list[args or kwargs]
        print("Getting from cache")
        return cache_list[args]
    return inner
