from typing import Callable


def cache(func: Callable) -> Callable:
    cache_saved_results = {}

    def wrapper(*args) -> any:
        if args in cache_saved_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_saved_results[args] = func(*args)
        return cache_saved_results[args]
    return wrapper
