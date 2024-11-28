from typing import Callable


def cache(func: Callable) -> Callable:

    cashed_data = {}

    def wrapper(*args) -> None:

        cash_data_check = args

        if cash_data_check in cashed_data:
            print("Getting from cache")
            return cashed_data.get(cash_data_check)
        else:
            result = func(*args)
            cashed_data.update({cash_data_check: result})
            print("Calculating new result")
            return result

    return wrapper
