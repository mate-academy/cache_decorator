from typing import Callable, Any


def cache(func: Callable) -> Callable:

    my_cache = {}

    def inner(*args) -> Any:

        if f"{args}{func.__name__}" in my_cache:
            print("Getting from cache")
            return my_cache[f"{args}{func.__name__}"]

        print("Calculating new result")
        result = func(*args)
        my_cache[f"{args}{func.__name__}"] = result
        return result

    return inner
