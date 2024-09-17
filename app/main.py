from typing import Callable


def cache(func: Callable) -> Callable:
    result = []

    def wrapper(*args, **kwargs) -> list:
        if func(*args, **kwargs) not in result:
            result.append(func(*args, **kwargs))
            print("Calculating new result")
        else:
            print("Getting from cache")
        return result

    return wrapper
