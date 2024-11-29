from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    stored_results = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        if args not in stored_results:
            print("Calculating new result")
            stored_results[args] = func(*args)
        else:
            print("Getting from cache")
        return stored_results[args]

    return wrapper
