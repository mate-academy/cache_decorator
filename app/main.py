from typing import Callable


def cache(func: Callable) -> Callable:

    results_storage = {}

    def inner_checker(*args) -> str:

        key = args
        if key in results_storage:
            print("Getting from cache")
            return results_storage[key]
        else:
            print("Calculating new result")
            value = func(*args)
            results_storage[key] = value
            return value

    return inner_checker
