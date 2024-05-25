from typing import Callable
from typing import Any


def cache(func: Callable) -> Callable:
    result_dict = {}

    def wrapper(*args, **kwargs) -> Any:
            if args in result_dict:
                print("Getting from cache")
                return result_dict[args]
            else:
                print("Calculating new result")
                result = func(*args)
                result_dict[args] = result
                return result
    return wrapper
