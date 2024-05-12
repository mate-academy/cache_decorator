from typing import Callable
import functools


def cache(func: Callable) -> Callable:
    results = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        if args not in results:
            results[args] = func(*args, **kwargs)
            print("Calculating new result")
        elif kwargs and kwargs not in results:
            results[kwargs] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return results[args]
    return wrapper
