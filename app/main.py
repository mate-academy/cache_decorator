from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args) -> None:
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
            res_of_func = func(*args)
            data[args] = res_of_func
            return res_of_func

    return wrapper
