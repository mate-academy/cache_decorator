from typing import Callable

from functools import wraps


def cache(func: Callable) -> Callable:
    cash_dict = {}

    @wraps(func)
    def compare_cash(*args) -> dict:
        func_name = func.__name__

        if (func_name, args) not in cash_dict:
            print("Calculating new result")
            result = func(*args)
            cash_dict[(func_name, args)] = result
            return result
        else:
            print("Getting from cache")
            return cash_dict[(func_name, args)]

    return compare_cash
