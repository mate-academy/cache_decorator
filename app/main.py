from typing import Callable


def cache(func: Callable) -> Callable:
    data = {}

    def wrapper(*args) -> None:
        if args not in data:
            print("Calculating new result")
            result = func(*args)
            data[args] = result
            return result
        else:
            print("Getting from cache")
            return data[args]
    return wrapper