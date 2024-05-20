from typing import Callable


def cache(func: Callable) -> Callable:
    cash = {}

    def inner(*args: Callable) -> Callable:
        if args not in cash:
            print("Calculating new result")
            cash[args] = func(*args)
        else:
            print("Getting from cache")
        return cash[args]
    return inner
