from typing import Tuple, Any, Callable


def cache(func: Callable) -> Callable:
    cache_store = {}

    def wrapper(*args: Tuple) -> Any:
        key = (func, args)
        if key in cache_store:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args)
            cache_store[key] = result
        return cache_store[key] if key in cache_store else key in cache_store
    return wrapper
