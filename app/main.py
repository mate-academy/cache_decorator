from typing import Callable


def cache(func: Callable) -> Callable:
    cashe_dict = {}

    def inner(*args, **kwargs) -> Callable:
        if args in cashe_dict:
            print("Getting from cache")
        else:
            print("Calculating new result")
            cashe_dict[args] = func(*args)
        return cashe_dict[args]
    return inner
