from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        if (func, *args) not in storage:
            answer = func(*args)
            storage[(func, *args)] = answer
            print("Calculating new result")
        else:
            print("Getting from cache")
        return storage[(func, *args)]
    return wrapper
