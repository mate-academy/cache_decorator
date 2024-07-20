from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cash_dict = dict()

    @functools.wraps(func)
    def inner(*args, **kwargs) -> Any:
        key = (func.__name__, args)
        if key in cash_dict:
            print("Getting from cache")
            return cash_dict[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cash_dict[key] = result
        return result

    return inner
