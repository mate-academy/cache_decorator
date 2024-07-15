from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args) -> int:
        key = (func.__name__, args)
        if key in results:
            print("Getting from cache")
            return results.get(key)
        print("Calculating new result")
        results[key] = func(*args)
        return results.get(key)

    return wrapper
