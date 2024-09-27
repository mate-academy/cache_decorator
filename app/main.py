from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> Any:
        data = (args, tuple(sorted(kwargs.items())))

        if data not in cache_data:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_data[data] = result
        else:
            print("Getting from cache")

        return cache_data[data]

    return wrapper
