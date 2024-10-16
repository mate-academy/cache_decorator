from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any) -> Any:
        cache_key = args
        if cache_key in cache_storage:
            print("Getting from cache")
            return cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_storage[cache_key] = result
            return result

    return wrapper
