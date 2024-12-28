from typing import Callable


def cache(func: Callable) -> Callable:
    cache_history = {}

    def wrapper(*args):
        nonlocal cache_history

        if args in cache_history.keys():
            print("Getting from cache")
            return cache_history[args]
        else:
            print("Calculating new result")
            result = func(args)
            cache_history["args"] = result
            return result
    return wrapper
