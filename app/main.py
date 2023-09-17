from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result_cache = {}

    def wrapper(*args, **kwargs) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in result_cache:
            print("Getting from cache")
            result = result_cache[key]
        else:
            result = func(*args, **kwargs)
            result_cache[key] = result
            print("Calculating new result")

        return result

    return wrapper
