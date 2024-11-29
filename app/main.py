from typing import Callable, Any

def cache(func: Callable) -> Callable:
    cashed_data = {}

    def wrapper(*args) -> None:

        cache_data_check = args

        if cache_data_check in cashed_data:
            print("Getting from cache")
        else:
            result = func(*args)
            cashed_data.update({cache_data_check: result})
            print("Calculating new result")
        return cashed_data[cache_data_check]
    return wrapper
