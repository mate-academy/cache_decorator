from typing import Callable
from functools import wraps


def cache(func: Callable) -> Callable:
    cache = {}

    @wraps(func)
    def wrapper(*args, **kwargs) -> int | str:
        arguments = args if args else kwargs
        if arguments in cache:
            print("Getting from cache")
            return cache.get(arguments)
        else:
            print("Calculating new result")
            cache[arguments] = func(*args, **kwargs)
            return cache[arguments]

    return wrapper
