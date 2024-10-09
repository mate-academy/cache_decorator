from typing import Callable


def cache(func: Callable) -> Callable:

    store = {}

    def wrapped(*args) -> Callable:
        if args in store:
            print("Getting from cache")
            return store[args]
        else:
            print("Calculating new result")
            result = func(*args)
            store[args] = result
            return result
    return wrapped
