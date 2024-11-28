from typing import Callable


def cache(func: Callable) -> Callable:

    cash_data_check = {}

    def wrapper(*args) -> None:

        nonlocal cash_data_check
        cashed_data = args

        if cashed_data in cash_data_check:
            print("Getting from cache")
            return cash_data_check.get(cashed_data)
        else:
            result = func(*args)
            cash_data_check.update({cashed_data: result})
            print("Calculating new result")
            return result

    return wrapper
