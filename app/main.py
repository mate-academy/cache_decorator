from typing import Callable


def cache(func: Callable) -> Callable:
    results_cache = {}

    def wrapper(*args) -> Callable:
        if args not in results_cache:
            results_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results_cache[args]
    return wrapper
