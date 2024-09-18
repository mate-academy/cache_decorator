from typing import Callable


def cache(func: Callable) -> Callable:

    result_storage = {}

    def wrapper(*args) -> Callable:
        result = None
        if args in result_storage:
            print("Getting from cache")
            result = result_storage[args]
        else:
            print("Calculating new result")
            result_storage[args] = func(*args)
            result = result_storage[args]
        return result
    return wrapper
