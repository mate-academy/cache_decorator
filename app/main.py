from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_dict = {}

    def wrapper(*args: Any) -> Any:
        if args in cached_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_dict[args] = func(*args)
        return cached_dict[args]
    return wrapper
