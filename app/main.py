import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_memory = dict()
    functools.wraps(func)

    def wrapper(*args, **kwargs) -> Any:
        keyword = ""
        for arg in args:
            keyword += str(arg)

        if keyword in cache_memory.keys():
            print("Getting from cache")
        else:
            print("Calculating new result")
            cache_memory[keyword] = func(*args, **kwargs)

        return cache_memory[keyword]
    return wrapper
