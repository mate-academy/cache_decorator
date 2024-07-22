from typing import Callable


def cache(func: Callable) -> Callable:
    buffer = {}

    def wrapper(*args, **kwargs) -> Callable:
        check = (*args, *kwargs)
        if buffer.get((*args, *kwargs)) is None:
            buffer[check] = func(*args, *kwargs)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return buffer[check]

    return wrapper
