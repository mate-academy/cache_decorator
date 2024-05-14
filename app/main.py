from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args: Any) -> Any:
        if args not in cache_storage:
            cache_storage[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return cache_storage[args]

    return wrapper
