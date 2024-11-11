from typing import Callable, Dict, Tuple, Any


def cache(func: Callable) -> Callable:
    cache_storage: Dict[Tuple, Any] = {}

    def wrapper(*args) -> any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result
    return wrapper
