from typing import Callable, Any


def cache(func: Callable) -> Callable:
    uniques_names_functions = {}

    def inner(*args) -> Any:
        if args not in uniques_names_functions:
            result_function = func(*args)
            uniques_names_functions[args] = result_function
            print("Calculating new result")
        else:
            print("Getting from cache")
        return uniques_names_functions[args]
    return inner
