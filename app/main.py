from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args) -> Any:
        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            result[args] = func(*args)
            print("Calculating new result")
            return result[args]
    return wrapper
