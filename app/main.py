from typing import Callable, Any


def cache(func: Callable) -> Callable:
    uniques_names_functions = {}

    def inner(*args) -> Any:
        if args in uniques_names_functions.keys():
            print("Getting from cache")
            return uniques_names_functions[args]
        else:
            uniques_names_functions[args] = func(*args)
            print("Calculating new result")
            return uniques_names_functions[args]
    return inner
