from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cash_store = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(kwargs.items()))
        if key in cash_store:
            print("Getting from cache")
            result = cash_store[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cash_store[key] = result
        return result

    return wrapper
