from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cache_storage: dict[tuple, Any] = {}

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