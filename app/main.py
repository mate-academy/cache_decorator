from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = args
        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            result[key] = func(*args, **kwargs)
            print("Calculating new result")
        return result[key]
    return wrapper
