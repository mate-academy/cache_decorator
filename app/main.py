from typing import Callable


def cache(func: Callable) -> Callable:
    collected_data = {}

    def wrapper(*args) -> int:

        if args not in collected_data:
            function_result = func(*args)
            collected_data[args] = function_result
            print("Calculating new result")
            return function_result

        print("Getting from cache")
        return collected_data[args]

    return wrapper
