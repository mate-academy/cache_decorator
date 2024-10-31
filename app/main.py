from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    calculated_data = []

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        for value in args:
            if isinstance(value, (list, set, dict)):
                return None
        for args_save, kwargs_save, result_save in calculated_data:
            if args_save == args and kwargs_save == kwargs:
                print("Getting from cache")
                return result_save
        result = func(*args, **kwargs)
        calculated_data.append((args, kwargs, result))
        print("Calculating new result")
        return result
    return wrapper
