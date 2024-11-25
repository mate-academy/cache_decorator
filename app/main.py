from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_var = {}

    def wrappen(*args) -> int:
        if args in cache_var:
            print("Getting from cache")
            return cache_var[args]
        else:
            result = func(*args)
            cache_var[args] = result
            print("Calculating new result")
            return result
    return wrappen
