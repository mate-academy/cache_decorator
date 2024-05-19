from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    seve_res = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if args in seve_res:
            print("Getting from cache")
            res = seve_res[args]
        else:
            res = func(*args, **kwargs)
            seve_res[args] = res
            print("Calculating new result")
        return res
    return wrapper
