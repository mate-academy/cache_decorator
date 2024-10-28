from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def decorate(*args) -> None:
        if len(result) == 0 or args not in result:
            print("Calculating new result")
            new_value = func(*args)
            result[args] = new_value
            return new_value
        else:
            print("Getting from cache")
            return result[args]
    return decorate
    return result
