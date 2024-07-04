from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    results = {}

    @wraps(func)
    def wrap(*args, **kwargs) -> int:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            results[args] = func(*args, **kwargs)
            print("Calculating new result")
            return results[args]

    return wrap
