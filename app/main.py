from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any) -> Any:
        if args in cache_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_dict[args] = func(*args)
        return cache_dict[args]
    return wrapper
