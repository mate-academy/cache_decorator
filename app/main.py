from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in cache_dict:
            print("Calculating new result")
            cache_dict[args] = func(*args, *kwargs)
            return cache_dict[args]
        print("Getting from cache")
        return cache_dict[args]

    return wrapper
