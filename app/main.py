from functools import wraps
from typing import Callable, Any, Tuple


def cache(func: Callable) -> Callable:
    cache_store = {}

    @wraps(func)
    def wrapper(*args: Tuple[Any, ...]) -> Any:
        if args in cache_store:
            print("Getting from cache")
            result = cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
        return result

    return wrapper
