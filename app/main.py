from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrapper(*args, **kwargs) -> Callable:
        nonlocal results
        key = args if args else tuple(kwargs.items())
        if key in results:
            print("Getting from cache")
            return results[key]
        print("Calculating new result")
        results[key] = func(*args, **kwargs)
        return results[key]

    return wrapper
