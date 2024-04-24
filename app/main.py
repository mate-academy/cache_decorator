from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    functions_cache_dict = {}

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in functions_cache_dict:
            print("Getting from cache")
        else:
            functions_cache_dict[key] = func(*args, **kwargs)
            print("Calculating new result")
        return functions_cache_dict[key]

    return wrapper
