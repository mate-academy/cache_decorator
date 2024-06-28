from typing import Any, Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results_cache = {}

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        input_key = (args, frozenset(kwargs.items()))

        if input_key in results_cache:
            print("Getting from cache")
            return results_cache[input_key]

        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            results_cache[input_key] = result
            return result

    return wrapper
