from typing import Callable


def cache(func: Callable) -> Callable:
    saved_results = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in saved_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            saved_results[args] = func(*args)
        return saved_results[args]

    return wrapper
