from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    a = []
    @wraps(func)
    def wrapper(*args, **kwargs) -> any:
        result = func(*args, **kwargs)
        if result not in a:
            a.append(result)
            print("Calculating new result")
        else:
            print("Getting from cache")
    return wrapper
