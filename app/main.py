from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> dict:
        key = (args, frozenset(kwargs.items()))

        if key in result:
            print("Getting from cache")
            cashed_results = result[key]
        else:
            print("Calculating new result")
            cashed_results = func(*args, **kwargs)
            result[key] = cashed_results

        return cashed_results

    return inner
