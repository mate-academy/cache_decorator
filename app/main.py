import functools
from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> any:
        kwargs_value = tuple()
        for key, value in kwargs.items():
            kwargs_value += (key, value)

        if (args, kwargs_value) in cached_data:
            print("Getting from cache")
            return cached_data[(args, kwargs_value)]

        result_of_decorated_function = func(*args, **kwargs)
        cached_data[(args, kwargs_value)] = result_of_decorated_function
        print("Calculating new result")
        return result_of_decorated_function

    return wrapper
