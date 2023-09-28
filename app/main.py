from typing import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def inner(*args, **kwargs) -> None:
        key = args

        if key in cache_dict:
            print("Getting from cache")
            return cache_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_dict[key] = result

            return result

    return inner
