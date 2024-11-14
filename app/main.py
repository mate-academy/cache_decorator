from typing import Callable


def cache(func: Callable) -> Callable:
    parameters = {}

    def collector(*args) -> None:
        if args not in parameters:
            parameters[args] = func(*args)
            print("Calculating new result ")
            return func(*args)
        else:
            print("Getting from cache")
            return parameters[args]


    return collector





