from typing import Callable


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args, **kwargs) -> Callable:
        parameters = tuple(args)
        if parameters not in cached_data.keys():
            result = func(*args, **kwargs)
            cached_data[parameters] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return cached_data.get(parameters)
    return wrapper
