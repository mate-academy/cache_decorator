from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def inner(*args, **kwargs) -> int:
        array = tuple([*args])
        if array in memory.keys():
            print("Getting from cache")
            return memory[array]
        memory[array] = func(*args, **kwargs)
        print("Calculating new result")
        return memory[array]
    return inner
