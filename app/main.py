from typing import Tuple, Any, Callable, Dict
from functools import wraps


def cache(func: Callable) -> Callable:
    cache_store: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args: Tuple, **kwargs: Dict) -> Any:
        key = (func.__name__, args, tuple(sorted(kwargs.items())))
        if key not in cache_store:
            print("Calculating new result")
            cache_store[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return cache_store[key]
    return wrapper
