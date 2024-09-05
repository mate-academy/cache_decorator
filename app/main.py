from functools import wraps
from typing import Callable, Any, Dict, Tuple


def cache(func: Callable) -> Callable:
    results: Dict[Tuple, Any] = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> [int, list]:
        key = (args , frozenset(kwargs.items()) , func.__name__)
        if key in results :
            print("Getting from cache")
        else :
            results[key] = func(*args , **kwargs)
            print("Calculating new result")
        return results[key]

    return wrapper
