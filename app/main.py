from typing import Callable


def cache(func: Callable) -> Callable:
    cachet = {}

    def wrapper(*args) -> int | str:
        if args in cachet:
            print("Getting from cache")
            return cachet.get(args)
        else:
            print("Calculating new result")
            cachet[args] = func(*args)
            return cachet[args]

    return wrapper
