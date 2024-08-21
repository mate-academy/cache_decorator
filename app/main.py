from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    saved_data = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key_args = (args, *sorted(kwargs.items()), func.__name__)

        if key_args not in saved_data:
            saved_data[key_args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return saved_data[key_args]

    return inner
