from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> int:
        key = (func.__name__, args)
        if key not in results:
            print("Calculating new result")
            results[key] = func(*args)
        else:
            print("Getting from cache")
        return results.get(key)

    return wrapper
