from typing import Callable


def cache(func: Callable) -> Callable:
    save_parameters = {}

    def inner(*args) -> int | float:
        if args in save_parameters:
            print("Getting from cache")
            return save_parameters[args]
        else:
            result = func(*args)
            print("Calculating new result")
            save_parameters[args] = result
            return result
    return inner
