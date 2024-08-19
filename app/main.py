from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def wrapper(*args) -> Any:

        cash_item = tuple(args)
        if cash_item not in cash_dict:
            result = func(*args)
            cash_dict[cash_item] = result
            print("Calculating new result")
        else:
            result = cash_dict[cash_item]
            print("Getting from cache")
        return result

    return wrapper
