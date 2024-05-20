from typing import Callable


def cache(func: Callable) -> Callable:
    cached_dict = {}

    def wrapper(*args, **kwargs) -> None:
        if args in cached_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cached_dict[args] = func(*args, **kwargs)
        return cached_dict[args]
    return wrapper
