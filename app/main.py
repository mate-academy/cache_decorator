from typing import Callable, Any


def cache(func: Callable) -> Callable:
    collected_data = {}

    def wrapper(*args) -> Any:

        if args not in collected_data:
            function_result = func(*args)
            collected_data[args] = function_result
            print("Calculating new result")
        else:
            print("Getting from cache")

        return collected_data[args]

    return wrapper
