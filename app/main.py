from typing import Callable


def cache(func: Callable) -> Callable:
    def inner(*args, **kwargs) -> Callable:
        if not hasattr(func, "storage"):
            func.storage = {}
        key = (args, tuple(kwargs.items()))
        if key in func.storage:
            print("Getting from cache")
            return func.storage[key]
        func.storage[key] = func(*args, **kwargs)
        print("Calculating new result")
        return func.storage[key]
    return inner
