from typing import Callable, Any


def cache(func: Callable) -> Any:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))

        if key in cache_storage:
            print("Getting from cache")
            return cache_storage[key]
        else:
            print("Calculating new result")
            cache_storage[key] = func(*args, **kwargs)
            return cache_storage[key]

    return wrapper
