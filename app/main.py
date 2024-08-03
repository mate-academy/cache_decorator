from typing import Callable


def cache(func: Callable) -> Callable:

    runs = {}
    def wrapper(*args, **kwargs) -> int:
        if args in runs:
            print("Getting from cache")
            return runs[args]
        else:
            result = func(*args, **kwargs)
            runs[args] = result
            print("Calculating new result")
            return result
    return wrapper
