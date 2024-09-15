from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args) -> int:
        if args not in result:
            result[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")
        return func(*args) if args not in result else result[args]
    return inner
