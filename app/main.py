from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        is_cachable = True
        for arg in args:
            if isinstance(arg, (list, dict, set)):
                is_cachable = False
                break

        if is_cachable:
            for arguments, result in cached_results.items():
                if arguments == args:
                    print("Getting from cache")
                    return result
        print("Calculating new result")
        calculated_result = func(*args)
        if is_cachable:
            cached_results[args] = calculated_result
        return calculated_result

    return wrapper
