from typing import Callable


def cache(func: Callable) -> Callable:
    cachces = {}

    def inner(*args, **kwargs) -> any:
        key = (*args, *kwargs.items())
        if key in cachces:
            print("Getting from cache")
            return cachces[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cachces[key] = result
            return result
    return inner
