from typing import Callable


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Callable:
        nonlocal cache_storage
        if args in cache_storage:
            print("Getting from cache")
            return cache_storage[args]
        else:
            func_result = func(*args, **kwargs)
            cache_storage.update({args: func_result})
            print("Calculating new result")
            return func_result

    return wrapper
