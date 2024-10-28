from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    saved_results = {}

    @wraps(func)
    def wrapper(*args: Any) -> Any:
        if args in saved_results:
            print("Getting from cache")
            return saved_results[args]
        else:
            result = func(*args)
            saved_results[args] = result
            print("Calculating new result")
            return result

    return wrapper
