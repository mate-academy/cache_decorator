from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    new_dict = {}

    @functools.wraps(func)
    def wrapper(*args: (int, tuple)) -> Any:
        if args not in new_dict:
            print("Calculating new result")
            new_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return new_dict[args]
    return wrapper
