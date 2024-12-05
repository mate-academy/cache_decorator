from typing import Callable


def cache(func: Callable) -> Callable:

    our_dict = {}

    def wrapper(*args) -> int:

        if args not in our_dict:
            print("Calculating new result")
            result = func(*args)
            our_dict[args] = result
        else:
            print("Getting from cache")

        return our_dict[args]

    return wrapper
