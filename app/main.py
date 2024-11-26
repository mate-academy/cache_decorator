from typing import Callable


def cache(func: Callable) -> Callable:
    cache_saved_results = {}

    def wrapper(*args) -> any:
        if args in cache_saved_results:
            print("Getting from cache")
            return cache_saved_results[args]
        print("Calculating new result")
        return cache_saved_results.setdefault(args, func(*args))
    return wrapper
