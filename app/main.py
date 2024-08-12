from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> int:
        key = args + tuple(kwargs.items())
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            print("Calculating new result")
            return result
    return wrapper
