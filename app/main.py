from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:
        if args in storage.keys():
            print("Getting from cache")
        else:
            storage[args] = func(*args)
            print("Calculating new result")
        return storage[args]
    return inner
