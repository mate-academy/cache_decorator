from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> any:
        if args in cached_data:
            print("Getting from cache")
            return cached_data[args]

        res = func(*args)
        cached_data[args] = res
        print("Calculating new result")
        return res

    return wrapper
