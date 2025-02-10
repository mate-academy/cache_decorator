from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        key = (args, tuple(kwargs.items()))
        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_dict[key] = result
        return result

    return wrapper
