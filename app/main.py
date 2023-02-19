from typing import Callable, Any


def cache(func: Callable) -> Any:
    data = {}

    def inner(*args) -> Any:
        if args in data:
            print("Getting from cache")
            return data[args]
        else:
            print("Calculating new result")
        data[args] = func(*args)
        return data[args]
    return inner
