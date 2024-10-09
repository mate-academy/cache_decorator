from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    store = {}

    @wraps(func)
    def wrapped(*args, **kwargs) -> dict:

        key = (args, frozenset(kwargs.items()))

        if key in store:
            print("Getting from cache")
            return store[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        store[key] = result
        return result

    return wrapped
