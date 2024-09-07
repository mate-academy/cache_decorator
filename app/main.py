from typing import Callable


def cache(func: Callable) -> Callable:

    cashe = {}

    def wrapper(*args) -> Callable:
        if args in cashe:
            print("Getting from cache")
            return cashe[args]
        print("Calculating new result")
        cashe[args] = func(*args)
        return cashe[args]
    return wrapper
