from typing import Callable


def cache(func: Callable) -> Callable:
    result_dict = {}

    def inner(*args, **kwargs) -> int:
        key = (args, tuple(sorted(kwargs.items())))
        if key in result_dict:
            print("Getting from cache")
            return result_dict[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            result_dict[key] = result
            return result
    return inner
