from typing import Callable


def cache(func: Callable) -> Callable:
    func_cache = {}

    def wrapper(*args) -> Callable:
        if args in func_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            func_cache[args] = func(*args)
        return func_cache[args]

    return wrapper
