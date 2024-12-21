from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def inner(*args, **kwargs) -> func:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in results:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result
        else:
            print("Getting from cache")
            return results[key]
    return inner
