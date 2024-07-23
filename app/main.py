from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        for arguments, result in cached_results.items():
            if arguments == args:
                print("Getting from cache")
                return result
        print("Calculating new result")
        calculated_result = func(*args)
        cached_results[args] = calculated_result
        return calculated_result

    return wrapper
