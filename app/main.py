from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs) -> Any:
        if args not in result_dict:
            print("Calculating new result")
            result_dict[args] = func(*args)
        else:
            print("Getting from cache")
        return result_dict[args]
    return wrapper
