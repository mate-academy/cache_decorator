from typing import Callable


def cache(func: Callable) -> Callable:
    result = {}

    def wrapper(*args) -> str:
        if isinstance(args, (int, float, bool, str, tuple)):
            if args in result:
                print("Getting from cache")
                return result[args]

        new_result = func(*args)
        result[args] = new_result
        print("Calculating new result")
        return result[args]

    return wrapper
