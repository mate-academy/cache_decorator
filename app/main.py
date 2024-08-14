from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> dict:
        key = (args, frozenset(kwargs.items()))

        if key in result:
            print("Getting from cache")
            return result[key]
        else:
            print("Calculating new result")
            func_result = func(*args, **kwargs)
            result[key] = func_result
            return func_result

    return inner
