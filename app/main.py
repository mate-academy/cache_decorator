from typing import Callable


def cache(func: Callable) -> Callable:
    res_dict = {}

    def inner(*args) -> str:
        if args not in res_dict:
            print("Calculating new result")
            result = func(*args)
            res_dict[args] = result
        else:
            print("Getting from cache")
        return res_dict[args]
    return inner
