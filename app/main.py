from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key not in cache_dict:
            print("Calculating new result")
            cache_dict[key] = func(*args, **kwargs)
        else:
            print("Getting from cache")

        return cache_dict[key]
    return wrapper
