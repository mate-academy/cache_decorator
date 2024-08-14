from functools import wraps
from typing import Callable, Any


def cache(func: Callable) -> Callable:

    """ If data calculations is repeated it is good to cache result
     of calculations to save resources without additional calculations.
     Usage: @cache annotation to your function
     Restrictions: Do not use mutable data or kwargs"""

    arguments_cache_dict = {}

    def __check_input(*args, **kwargs) -> Any:
        for arg in args:
            if isinstance(arg, (list, set, dict)):
                raise TypeError(
                    f"Only IMMUTABLE types allowed, got {type(arg).__name__}"
                )

    def __check_cache(func_obj: Callable, *args) -> dict:
        nonlocal arguments_cache_dict
        if args not in arguments_cache_dict:
            print("Calculating new result")
            arguments_cache_dict[args] = func_obj(*args)
            return arguments_cache_dict[args]
        else:
            print("Getting from cache")
            return arguments_cache_dict[args]

    @wraps(func)
    def wrapper(*args) -> Any:
        nonlocal arguments_cache_dict
        __check_input(args)
        return __check_cache(func, *args)

    return wrapper
