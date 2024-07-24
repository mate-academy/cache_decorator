from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in cached_results:
            print("Getting from cache")
            result = cached_results[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cached_results[args] = result

        return result

    return wrapper
