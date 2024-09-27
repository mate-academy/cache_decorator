from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_data = {}

    def wrapper(*args) -> Any:
        if args not in cache_data:
            print("Calculating new result")
            result = func(*args)
            cache_data[args] = result
        else:
            print("Getting from cache")

        return cache_data[args]

    return wrapper
