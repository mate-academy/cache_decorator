from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args) -> Callable:
        nonlocal results
        if func.__name__ + str(args) in results:
            print("Getting from cache")
            return results[func.__name__ + str(args)]
        else:
            print("Calculating new result")
            results[func.__name__ + str(args)] = func(*args)
            return results[func.__name__ + str(args)]
    return wrapper
