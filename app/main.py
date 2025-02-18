from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args, **kwargs) -> None:
        if args in cache_dict.keys():
            print("Getting from cache")
            return cache_dict[args]

        result = func(*args, **kwargs)
        cache_dict[args] = result
        print("Calculating new result")

        return result
    return wrapper
