from typing import Callable
from functools import wraps


def cache(func: Callable[..., int]) -> Callable[..., int]:
    """
    A decorator function that caches the results of a given function.
    """
    cache_data = {}

    @wraps(func)
    def wrapper(*args: tuple) -> int:
        if not all(
            isinstance(arg, (int, str, tuple, frozenset)) for arg in args
        ):
            raise ValueError(
                "All arguments must be immutable"
            )

        if args in cache_data:
            print("Getting from cache")
            return cache_data[args]
        else:
            print("Calculating new result")

        result = func(*args)
        cache_data[args] = result
        return result

    return wrapper
