from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash = {}

    def inner(*args) -> Any:
        if args in cash:
            print("Getting from cache")
            return cash[args]
        else:
            print("Calculating new result")
            cash[args] = func(*args)
            return cash[args]

    return inner
#
