from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    seve_res = {}

    def wrapper(*args) -> Any:
        if args in seve_res:
            print("Getting from cache")
            res = seve_res[args]
        else:
            res = func(*args)
            seve_res[args] = res
            print("Calculating new result")
        return res
    return wrapper
