from functools import wraps
from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    @wraps(func)
    def inner(*args) -> int:
        if (func.__name__, args) not in result:
            result[(func.__name__, args)] = \
                result.get((func.__name__, args), func(*args))
            print("Calculating new result")
        else:
            print("Getting from cache")

        return result[(func.__name__, args)]

    return inner
