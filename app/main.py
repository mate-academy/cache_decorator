from typing import Any


def cache(func: Any) -> Any:
    cache_data = {}

    def wrapper(*args) -> Any:
        if args in cache_data:
            print("Getting from cache")
        else:
            cache_data[args] = func(*args)
            print("Calculating new result")
        return cache_data[args]

    return wrapper
