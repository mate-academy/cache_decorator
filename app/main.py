from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:

    decorator_cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        args += tuple(kwargs.values())
        if args not in decorator_cache:
            print("Calculating new result")
            decorator_cache[args] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return decorator_cache[args]
    return wrapper
