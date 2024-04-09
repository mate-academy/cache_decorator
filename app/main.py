from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args, **kwargs) -> int:
        if args in result:
            print("Getting from cache")
        else:
            result[args] = func(*args, **kwargs)
            print("Calculating new result")
        return result[args]
    return wrapper
