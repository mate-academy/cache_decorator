import functools
from typing import Callable, Any


def cache(func: Callable) -> Callable:
    memory: dict = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        func_hash = (func.__name__, f"{args}{kwargs}")
        if func_hash not in memory:
            print("Calculating new result")
            memory[func_hash] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return memory[func_hash]

    return wrapper
