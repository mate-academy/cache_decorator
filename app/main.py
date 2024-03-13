from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args, **kwargs) -> Any:

        if cache_data.get(args) is not None:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_data[args] = func(*args, **kwargs)

        return cache_data[args]

    return wrapper
