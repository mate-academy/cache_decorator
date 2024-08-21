from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_data = {}

    def inner(*args) -> Any:
        if args not in saved_data:
            saved_data[args] = func(*args)
            print("Calculating new result")
        else:
            print("Getting from cache")

        return saved_data[args]

    return inner
