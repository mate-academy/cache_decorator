from typing import Callable


def cache(func: Callable) -> Callable:
    history = {}

    def wrapper(*args) -> Callable:
        if isinstance(args, (int, float, str, tuple)):
            if args in history:
                print("Getting from cache")
                return history[args]
            else:
                result = func(*args)
                print("Calculating new result")
                history[args] = result
                return result

    return wrapper
