from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_direct = {}

    def inner(*args) -> Any:
        if args in cache_direct:
            print("Getting from cache")
            return cache_direct[args]
        else:
            print("Calculating new result")
            res = func(*args)
            cache_direct[args] = res
            return res

    return inner
