from typing import Callable


def cache(func: Callable) -> Callable:
    data_base: dict[tuple, any] = {}

    def wrapper(*args, **kwargs) -> any:
        key = (args, tuple(kwargs.items()))
        if key in data_base:
            print("Getting from cache")
            return data_base[key]
        print("Calculating new result")
        data_base[key] = func(*args, **kwargs)
        return data_base[key]
    return wrapper
