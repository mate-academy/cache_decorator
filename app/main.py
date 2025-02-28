from typing import Callable, Any


def cache(func: Callable) -> Callable:
    func.cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, tuple(sorted(kwargs.items())))
        if key in func.cache_dict:
            print("Getting from cache")
            return func.cache_dict[key]
        else:
            print("Calculating new result")
            func.cache_dict[key] = func(*args, **kwargs)
            return func.cache_dict[key]
    return wrapper
