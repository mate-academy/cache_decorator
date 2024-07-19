from typing import Callable, Any
from functools import wraps

cached_data = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args) -> Callable:

        if func.__name__ in cached_data:
            if args in cached_data[func.__name__]:
                print("Getting from cache")
                return cached_data[func.__name__][args]
            else:
                return calc_data(*args)

        cached_data[func.__name__] = {}
        return calc_data(*args)

    def calc_data(*args) -> Any:
        print("Calculating new result")
        new_data = func(*args)
        cached_data[func.__name__][args] = new_data
        return new_data

    return wrapper
