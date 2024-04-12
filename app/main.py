from typing import Callable, Any


def cache(func: Callable) -> Callable:
    log = {}

    def inner(*args: Any) -> Callable:
        if args not in log:
            print("Calculating new result")
            log[args] = func(*args)
            return log[args]
        else:
            print("Getting from cache")
            return log[args]

    return inner
