from typing import Callable, Any


def cache(func: Callable) -> Callable:
    saved_cache = {}

    def wrapper(*args, **kwargs) -> Any:

        if args in saved_cache:
            print("Getting from cache")
            return saved_cache[args]

        print("Calculating new result")
        result = func(*args, **kwargs)
        saved_cache[args] = result

        return result
    return wrapper
