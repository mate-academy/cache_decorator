from typing import Callable, Any


def cache(func: Callable) -> Callable:
    storage = {}

    def inner(*args) -> Any:
        if args in storage:
            print("Getting from cache")
            return storage[args]

        print("Calculating new result")
        result = func(*args)
        storage[args] = result
        return result

    return inner
