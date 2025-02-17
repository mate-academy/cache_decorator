from typing import Callable, Any


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in dict_cache:
            print("Getting from cache")
            return dict_cache[key]
        else:
            print("Calculating new result")
            res = func(*args, **kwargs)
            dict_cache[key] = res
            return res
    return wrapper