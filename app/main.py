from typing import Callable

# Chache must be stored as "".join(func.__name__, args, kwargs)


def cache(func: Callable) -> Callable:
    chache = {}

    def wrapper(*args, **kwargs):
        func_code = str(func.__name__) + str(args) + str(kwargs)
        if func_code in chache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            chache[func_code] = result
        return chache[func_code]
    return wrapper
