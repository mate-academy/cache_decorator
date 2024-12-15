from typing import Any, Callable


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args) -> Any:
        if args not in result_cache:
            print("Calculating new result")
            result = func(*args)
            result_cache[args] = result
            return result
        else:
            print("Getting from cache")
            return result_cache[args]
    return wrapper
