from typing import Callable

new_set = {}

def cache(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        if (func.__name__, *args) in new_set:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            new_set[(func.__name__, *args)] = result
            return result
    return wrapper

