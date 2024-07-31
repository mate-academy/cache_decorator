from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(kwargs))
        if key not in cache_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[key] = result
            return cache_data[key]
        print("Getting from cache")
        return cache_data[key]

    return wrapper
