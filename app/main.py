from typing import Callable, Any


def cache(func: Callable) -> Any:
    result_dict = {}

    def wrapper(*args) -> Any:

        if args in result_dict.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_dict[args] = func(*args)

        return result_dict[args]

    return wrapper
