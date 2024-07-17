from typing import Callable, Any


def cache(func: Callable) -> Callable:
    former_functions = {}

    def wrapper(*args, **kwargs) -> Any:
        nonlocal former_functions
        values = tuple([value for value in kwargs.values()])
        arguments = (*args, *values)
        if (arguments, func) in former_functions:
            print("Getting from cache")
            return former_functions[(arguments, func)]
        else:
            print("Calculating new result")
            former_functions[(arguments, func)] = func(*args, **kwargs)
            return former_functions[(arguments, func)]

    return wrapper
