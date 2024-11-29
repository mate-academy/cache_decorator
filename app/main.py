from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    # {func: {args: result}}
    stored_results = {}

    @wraps(func)
    def wrapper(*args) -> dict:
        # print(stored_results)
        if args not in stored_results:
            print("Calculating new result")
            stored_results[args] = func(*args)
        else:
            print("Getting from cache")
        return stored_results[args]

    return wrapper
