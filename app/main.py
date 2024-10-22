from typing import Callable


def cache(func: Callable) -> Callable:
    cache_saved_results = {}

    def wrapper(*args) -> int:
        if args in cache_saved_results:
            print("Getting from cache")
            return cache_saved_results[args]
        print("Calculating new result")
        cache_saved_results[args] = func(*args)
        return cache_saved_results[args]
    return wrapper
