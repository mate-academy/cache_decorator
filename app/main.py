from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in results_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            results_cache[key] = func(*args, **kwargs)
        return results_cache[key]
    return wrapper
