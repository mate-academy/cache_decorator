from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args) -> Any:
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            print("Calculating new result")
            func_result = func(*args)
            cache_storage[args] = func_result
            return func_result

    return wrapper
