from typing import Callable, Dict, Tuple, Any


def cache(func: Callable) -> Callable:
    """
    A decorator that caches the results of function
    calls with immutable arguments.
    """
    cache_store: Dict[Tuple, Any] = {}

    def wrapper(*args) -> Any:
        if args in cache_store:
            print("Getting from cache")
            return cache_store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[args] = result
            return result

    return wrapper
