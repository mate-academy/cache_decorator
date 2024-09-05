from functools import wraps
from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    results: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> [int, list]:
        key = (args, frozenset(kwargs.items()))
        if key in results:
            print("Getting from cache")
            return results[key]
        else:
            result = func(*args, **kwargs)
            results[key] = result
            print("Calculating new result")
            return result

    return wrapper
