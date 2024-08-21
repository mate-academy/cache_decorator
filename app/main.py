from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_box = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (*args, *kwargs.items())
        if key in cache_box:
            print("Getting from cache")
            return cache_box[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_box[key] = result
        return result
    return wrapper
