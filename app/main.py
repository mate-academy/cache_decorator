from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.values())

        if key in stored_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_results[key] = func(*args, **kwargs)

        return stored_results[key]

    return wrapper
