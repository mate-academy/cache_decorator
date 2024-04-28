from typing import Callable


def cache(func: Callable) -> Callable:
    cached_results = {}

    def wrapper(*args, **kwargs) -> int:

        key = (args, frozenset(kwargs.items()))

        if key in cached_results:
            print("Getting from cache")
            result = cached_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached_results[key] = result

        return result

    return wrapper
