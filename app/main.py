from typing import Callable


def cache(func: Callable) -> Callable:

    tmp_cache = {}

    def inner(*args) -> None:
        if args in tmp_cache:
            print("Getting from cache")
            return tmp_cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            tmp_cache[args] = result
            return result
    return inner
