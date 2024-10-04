from typing import Any, Callable, Dict, Tuple
from functools import wraps


def cache(func: Callable) -> Callable:
    func_cache: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        key = (func.__name__, args, frozenset(kwargs.items()))
        if key in func_cache:
            print("Getting from cache")
            return func_cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func_cache[key] = result
            return result

    return wrapper
