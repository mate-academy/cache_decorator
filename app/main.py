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
            result = func(*args, **kwargs)
            cache_storage[key] = result
            return result

    return wrapper
