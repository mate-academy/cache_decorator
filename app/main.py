from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_history = {}

    def wrapper(*args: Any) -> Callable:
        nonlocal cache_history
        cache_key = args

        if cache_key in cache_history:
            print("Getting from cache")
            return cache_history[cache_key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_history[cache_key] = result
            return result
    return wrapper
