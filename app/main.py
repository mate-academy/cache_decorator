from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:
        if args not in storage:
            print("Calculating new result")
            func_result = func(*args)
            storage[args] = func_result
            return func_result
        else:
            print("Getting from cache")
            return storage[args]

    return inner
