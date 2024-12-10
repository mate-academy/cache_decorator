from typing import Callable


def cache(func: Callable) -> Callable:
    my_cash = {}

    def inner(*args) -> str:
        if args not in my_cash.keys():
            my_cash[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return my_cash[args]
    return inner
