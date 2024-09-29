from typing import Callable, Any, Dict


def cache(func: Callable) -> Callable:
    cache_storage: Dict[tuple, Any] = {}

    def wrapper(*args) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[args] = result
            return result

    return wrapper
