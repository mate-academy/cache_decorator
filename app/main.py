from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    dict_of_arguments = {}

    @wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key not in dict_of_arguments.keys():
            print("Calculating new result")
            dict_of_arguments[key] = func(*key)
        else:
            print("Getting from cache")
        return dict_of_arguments.get(key)
    return inner
