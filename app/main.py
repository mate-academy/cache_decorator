from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))

        if key in stored_results:
            print("Getting from cache")
        else:
            print("Calculating new result")
            stored_results[key] = func(*args, **kwargs)
        return stored_results[key]

    return wrapper
