from typing import Callable


def cache(func: Callable) -> Callable:
    result = dict()

    def inner(*args) -> int:
        if tuple(args) in result:
            print("Getting from cache")
            return result[tuple(args)]
        print("Calculating new result")
        result_of_func = func(*args)
        result.update({tuple(args): result_of_func})
        return result_of_func
    return inner
