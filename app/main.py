from typing import Any, Callable


def cache(func: Callable) -> Callable:
    store = {}

    def inner(*args) -> Any:
        if args in store:
            print("Getting from cache")
            return store[args]
        print("Calculating new result")
        result = store[args] = func(*args)
        return result

    return inner
