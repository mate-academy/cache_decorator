from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cached_data = {}

    def wrapper(*args) -> Any:
        cached_result = cached_data.get(args)

        if cached_result is not None:
            print("Getting from cache")
            return cached_result

        print("Calculating new result")
        cached_data[args] = func(*args)
        return cached_data[args]

    return wrapper
