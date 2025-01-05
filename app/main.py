from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> Any:
        func_name = f"{func.__name__}"

        if func_name not in cache_dict:
            cache_dict[func_name] = {}
        if args not in cache_dict[func_name]:
            cache_dict[func_name][args] = func(*args, **kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return cache_dict[func_name][args]
    return inner
