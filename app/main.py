from typing import Callable


def cache(func: Callable) -> Callable:
    parameters = {}

    def collector(*args) -> None:
        if args not in parameters:
            res = func(*args)
            parameters[args] = res
            print("Calculating new result")
            return res
        else:
            print("Getting from cache")
            return parameters[args]

    return collector
