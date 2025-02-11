from typing import Callable



def cache(func: Callable) -> Callable:
    used_functions = {}
    def wrapper(*args, **kwargs):
        key = (func.__name__, args, tuple(kwargs.items()))

        if key in used_functions:
            result = used_functions[key]
            print("Getting from cache")
        else:
            used_functions[key] = func(*args,**kwargs)
            result = used_functions[key]
            print("Calculating new result")
        return result
    return wrapper

