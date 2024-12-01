from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Any:
    results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = tuple(args) + tuple(*kwargs.items())
        if key in results:
            print("Getting from cache")
            return results[key]
        result = func(*args, **kwargs)
        results[key] = result
        print("Calculating new result")
        return result
    return wrapper
