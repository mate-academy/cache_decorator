from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_results = {}

    @wraps(func)
    def wrapper(*args) -> Any:
        if args in dict_results:
            print("Getting from cache")
        else:
            dict_results[args] = func(*args)
            print("Calculating new result")
        return dict_results[args]
    return wrapper
