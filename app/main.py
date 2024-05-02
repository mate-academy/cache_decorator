from typing import Callable


def cache(func: Callable) -> Callable:
    cache_results = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in cache_results:
            print("Getting from cache")
        else:
            cache_results[args] = func(*args, **kwargs)
            print("Calculating new result")
        return cache_results[args]
    return wrapper
