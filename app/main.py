from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_data = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in cache_data:
            print("Getting from cache")
            result = cache_data[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_data[args] = result
        return result

    return wrapper
