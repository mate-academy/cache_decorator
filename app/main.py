from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    result_list = []

    def wrapper(*args) -> Any:
        if all(isinstance(arg, (int, float, tuple, bool)) for arg in args):
            args_tuple = tuple(args)
            if args_tuple not in result_list:
                print("Calculating new result")
                result = func(args)
                result_list.extend([args_tuple, result])
                return result
            else:
                print("Getting from cache")
                return result_list[result_list.index(args_tuple) + 1]
    return wrapper
