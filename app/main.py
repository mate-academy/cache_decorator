from typing import Callable, Any
import time


def cache(func: Callable) -> Callable:
    repeat_arguments = {}

    def function_result(*args: tuple[Any]) -> int:
        if args in repeat_arguments:
            print("Getting from cache")
            return repeat_arguments[args]
        print("Calculating new result")
        result = func(*args)
        repeat_arguments[args] = result
        return result
    return function_result
