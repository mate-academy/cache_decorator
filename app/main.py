from typing import Callable


def cache(func: Callable) -> Callable:
    dict_cache = {}

    def inner(*args, **kwargs) -> Callable:
        if args in dict_cache:
            print("Getting from cache")
            return dict_cache[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            dict_cache[args] = result
            return result

    return inner
