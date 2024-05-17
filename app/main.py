from typing import Callable


def cache(func: Callable) -> Callable:
    memory = dict()

    def wrapper(*args, **kwargs) -> Callable:
        key = (*args, *kwargs.items())
        if key in memory:
            print("Getting from cache")
            return memory[key]
        else:
            memory_new = func(*args, **kwargs)
            memory[key] = memory_new
            print("Calculating new result")
            return memory_new

    return wrapper
