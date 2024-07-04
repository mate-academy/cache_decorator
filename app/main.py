from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def inner(*args, **kwargs) -> int:
        key = args
        if key in memory:
            print("Getting from cache")
            return memory[key]
        print("Calculating new result")
        result = func(*args)
        memory[key] = result
        return result
    return inner
