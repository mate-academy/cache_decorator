from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            new_result = func(*args)
            cache_storage[args] = new_result
            return new_result
    return wrapper
