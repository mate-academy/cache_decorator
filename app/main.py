from typing import Callable, Any, Tuple, Dict


def cache(func: Callable) -> Callable:
    cache_storage: Dict[Tuple, Any] = {}

    def inner(*args, **kwargs) -> Callable:
        key = (args, frozenset(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return inner
