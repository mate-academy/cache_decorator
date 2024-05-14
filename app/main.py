from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_cache = {}

    def inner(*args, **kwargs) -> Any:
        if args in result_cache:
            print("Getting from cache")
        else:
            print("Calculating new result")
            result_cache[args] = func(*args, **kwargs)
        return result_cache[args]

    return inner
