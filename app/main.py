from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args, **kwargs) -> Callable:
        parameters = tuple(args)
        if parameters not in cached_data.keys():
            result = func(*args, **kwargs)
            cached_data[parameters] = result
            return result
        else:
            return cached_data.get(parameters)
    return wrapper
