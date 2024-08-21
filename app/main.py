from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.values())

        if key in stored_results:
            print("Getting from cache")
            return stored_results[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            stored_results[key] = result
            return result

    return wrapper
