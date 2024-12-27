from typing import Callable


def cache(func: Callable) -> Callable:
    new_dict = {}

    def wrapper(*args, **kwargs) -> Callable:
        if (func.__name__, *args, str(**kwargs)) in new_dict:
            print("Getting from cache")
            return new_dict[(func.__name__, *args, str(**kwargs))]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            new_dict[(func.__name__, *args, str(**kwargs))] = result
            return result
    return wrapper