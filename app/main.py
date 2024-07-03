from typing import Callable


def cache(func: Callable) -> Callable:
    results = {}

    def wrap(*args) -> int:
        if args in results:
            print("Getting from cache")
            return results[args]
        else:
            results[args] = func(*args)
            print("Calculating new result")
            return results[args]

    return wrap
