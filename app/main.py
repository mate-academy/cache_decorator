from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_storage = {}

    def wrapper(*args, **kwargs) -> Any:
        cache_key = (func.__name__, args, tuple(sorted(kwargs.items())))

        if cache_key in cache_storage:
            print("Getting from cache")
            result = cache_storage[cache_key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_storage[cache_key] = result

        return result

    return wrapper
