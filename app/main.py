from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def wrap(*args) -> Any:

        if args in result:
            print("Getting from cache")
            return result[args]
        else:
            all_in = func(*args)
            result[args] = all_in
            print("Calculating new result")
            return all_in

    return wrap
