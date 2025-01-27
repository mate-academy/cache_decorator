from typing import Callable


def cache(func: Callable) -> Callable:
    memory = {}

    def wrapper(*args) -> None:
        if args not in memory:
            result = func(*args)
            memory[args] = result
            print("Calculating new result")
            return result
        else:
            print("Getting from cache")
            return memory[args]

    return wrapper
