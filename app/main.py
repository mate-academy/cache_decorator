from typing import Callable


def cache(func: Callable) -> Callable:
    res = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in res:
            print("Getting from cache")
            return res[key]
        else:
            print("Calculating new result")
            return res.setdefault(key, func(*args, **kwargs))

    return wrapper
