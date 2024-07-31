from typing import Callable


def cache(func: Callable) -> Callable:
    collected_data = {}

    def inner(*args, **kwargs) -> int:
        if args in collected_data:
            print("Getting from cache")
            return collected_data[args]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            collected_data[args] = result
            return result
    return inner
