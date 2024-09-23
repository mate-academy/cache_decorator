from typing import Callable


def cache(func: Callable) -> Callable:
    cashed_dict = {}

    def inner(*args, **kwargs) -> dict:
        key = (args, tuple(kwargs.items()))
        if key in cashed_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cashed_dict[key] = result
        return cashed_dict[key]
    return inner
