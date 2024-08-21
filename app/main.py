from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    saved_data = {}

    @wraps(func)
    def inner(*args) -> Any:
        if args not in saved_data:
            saved_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return saved_data[args]

    return inner
