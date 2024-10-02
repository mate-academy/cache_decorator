from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    dict_cache = {}

    @functools.wraps(func)
    def wrapper(*args: Any) -> Any:
        if args not in dict_cache:
            dict_cache[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return dict_cache[args]

    return wrapper
