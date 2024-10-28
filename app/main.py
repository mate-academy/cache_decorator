from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache = {}

    def inner(*args) -> Any:
        if args in cache:
            print("Getting from cache")
            return cache[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache[args] = result
        return result

    return inner
