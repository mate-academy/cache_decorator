from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_history = dict()

    def wrapper(*args) -> Any:

        if args in cache_history:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_history[args] = func(*args)

        return cache_history[args]

    return wrapper
