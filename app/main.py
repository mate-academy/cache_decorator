from typing import Callable, Any


def cache(func: Callable) -> Callable:
    my_cache = {}

    def wrapper(*args: Any) -> Any:
        if args in my_cache:
            print("Getting from cache")
        else:
            my_cache[args] = func(*args)
            print("Calculating new result")
        return my_cache[args]

    return wrapper
