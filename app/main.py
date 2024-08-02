from typing import Callable


def cache(func: Callable) -> Callable:
    result_cache = {}

    def inner(*args) -> Callable:
        if args in result_cache:
            print("Getting from cache")
            return result_cache.get(args)
        else:
            print("Calculating new result")
            result = func(*args)
            result_cache[args] = result
            return result

    return inner
