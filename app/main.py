from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    store = {}

    @wraps(func)
    def wrapped(*args, **kwargs) -> Any:

        key = (func.__name__, args, frozenset(kwargs.items()))

        if key in store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            store[key] = func(*args, **kwargs)

        return store[key]

    return wrapped
