from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    container = {}

    def wrapper(*args) -> Any:
        if args not in container:
            print("Calculating new result")
            result = func(*args)
            container[args] = result
            return result
        else:
            print("Getting from cache")
            return container[args]
    return wrapper
