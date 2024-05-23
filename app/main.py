from typing import Callable, Any


def cache(func: Callable) -> Callable:
    args_storage = {}

    def wrapper(*args) -> Any:
        if args in args_storage:
            print("Getting from cache")
            return args_storage[args]
        else:
            result = func(*args)
            args_storage[args] = result
            print("Calculating new result")
            return result
    return wrapper
