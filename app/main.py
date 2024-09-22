from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args) -> Callable:
        if not all(isinstance(arg, (list, set, dict)) for arg in args):
            if (func, *args) not in storage:
                answer = func(*args)
                storage[(func, *args)] = answer
                print("Calculating new result")
                return answer
            else:
                print("Getting from cache")
                return storage[(func, *args)]

    return wrapper
