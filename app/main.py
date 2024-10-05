from typing import Any, Callable, Dict, Tuple
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in func_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            func_cache[key] = func(*args, **kwargs)
        return func_cache[key]

    return wrapper
