from typing import Callable, Any
from functools import wraps


def cache(func: Callable) -> Callable:
    cash_dict = {}

    @wraps(func)
    def wrapper_cash(*args, **kwargs) -> Any:
        key = args + tuple(kwargs.items())
        if key in cash_dict:
            print("Getting from cache")
            return cash_dict[key]

        print("Calculating new result")
        cash_value = func(*args, **kwargs)
        cash_dict[key] = cash_value

        return cash_value

    return wrapper_cash
