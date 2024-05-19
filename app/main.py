from typing import Callable


def cache(func: Callable) -> Callable:
    cached = {}

    def inner(*args, **kwargs) -> Callable:
        key = f"{func.__name__} {str(args)} {str(kwargs)}"
        if cached.get(key) is None:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cached[key] = result
            return result
        print("Getting from cache")
        return cached[key]
    return inner
