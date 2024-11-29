from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> None:

        cache_data_check = args

        if cache_data_check in cached_data:
            print("Getting from cache")
        else:
            result = func(*args)
            cached_data.update({cache_data_check: result})
            print("Calculating new result")
        return cached_data[cache_data_check]
    return wrapper
