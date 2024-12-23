from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key not in results:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results[key] = result
            return result
        print("Getting from cache")
        return results[key]
    return inner
