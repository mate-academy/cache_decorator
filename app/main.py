from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (func, args, tuple(kwargs.items()))
        if key in cache_storage:
            print("Getting from cache")
        else:
            cache_storage[key] = func(*args)
            print("Calculating new result")
        return cache_storage[key]
    return inner
