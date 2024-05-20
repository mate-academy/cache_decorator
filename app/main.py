from typing import Callable


def cache(func: Callable) -> Callable:

    result_dict = {}

    def wrapper(*args) -> Callable:
        if args in result_dict:
            print("Getting from cache")
            return result_dict[args]
        else:
            result_dict[args] = func(*args)
            print("Calculating new result")
            return result_dict[args]

    return wrapper
