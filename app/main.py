from typing import Callable, Any


def cache(func: Callable) -> Callable:
    data_cash = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        nonlocal data_cash

        if key in data_cash:
            print("Getting from cache")
            return data_cash[key]
        else:
            func_result = func(*args, **kwargs)
            data_cash[key] = func_result
            print("Calculating new result")

            return func_result

    return wrapper
