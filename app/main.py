from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data = {}

    def inner(*args) -> Any:
        if args not in data:
            print("Calculating new result")
            result = func(*args)
            data[args] = result
            return result
        if args in data:
            print("Getting from cache")
            return data[args]

    return inner
