from typing import Callable, List, Any


def cache(func: Callable) -> Callable:
    result_list = {}

    def wrapper(*args) -> Any:
        result = args
        if result in result_list:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_list[result] = func(*args)
        return result_list[args]

    return wrapper
