from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    caches = {}

    @functools.wraps(func)
    def inner(*args) -> None:
        if args in caches:
            print("Getting from cache")
            return caches[args]
        else:
            print("Calculating new result")
            caches[args] = res = func(*args)
        return res

    return inner
