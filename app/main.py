from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def inner(*args: Any) -> Any:
        if args in cached_data:
            print("Getting from cache")
        else:
            cached_data[args] = func(*args)
            print("Calculating new result")

        return cached_data[args]

    return inner
