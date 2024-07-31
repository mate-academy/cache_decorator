from typing import Callable


def cache(func: Callable) -> Callable:
    all_result = {}

    def wrapper(*args) -> int:
        if args in all_result:
            print("Getting from cache")
            return all_result[args]
        else:
            print("Calculating new result")
            result = func(*args)
            all_result[args] = result
            return result

    return wrapper
