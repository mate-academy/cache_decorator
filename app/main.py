from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cached_results = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        is_cachable = True
        if kwargs:
            is_cachable = False
        else:
            for arg in args:
                if not isinstance(
                        arg, (bool, int, float, str, tuple, frozenset, bytes)
                ):
                    is_cachable = False
                    break

        if is_cachable:
            for arguments, result in cached_results.items():
                if arguments == args:
                    print("Getting from cache")
                    return result
        print("Calculating new result")
        calculated_result = func(*args, **kwargs)
        if is_cachable:
            cached_results[args] = calculated_result
        return calculated_result

    return wrapper
