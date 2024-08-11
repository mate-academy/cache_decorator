from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (func.__name__, args, tuple(sorted(kwargs.items())))

        if cache_key in cache_storage:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_storage[cache_key] = func(*args, **kwargs)

        return cache_storage[cache_key]

    return wrapper
