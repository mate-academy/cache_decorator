from typing import Callable


def cache(func: Callable) -> Callable:
    history = {}

    def wrapper(*args) -> Callable:
        if args in history:
            print("Getting from cache")
            result = history[args]
        else:
            result = func(*args)
            print("Calculating new result")
            history[args] = result

        return result

    return wrapper
