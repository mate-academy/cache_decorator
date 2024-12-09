from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args not in result:
            print("Calculating new result")
            result[args] = func(*args)
        else:
            print("Getting from cache")
        return result[args]
    return wrapper
