from typing import Callable


def cache(func: Callable) -> Callable:
    input_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        if args in input_dict:
            print("Getting from cache")
            return input_dict[args]
        else:
            print("Calculating new result")
            res_of_func = func(*args, **kwargs)
            input_dict[args] = res_of_func
            return res_of_func

    return wrapper
