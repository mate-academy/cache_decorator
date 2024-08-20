from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_box = {}

    def wrapper(*args, **kwargs) -> Any:
        if args in cache_box:
            print("Getting from cache")
            return cache_box[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cache_box[args] = result
        return result
    return wrapper
