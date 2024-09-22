from typing import Callable, Any


def cache(func: Callable) -> Callable:
    result = {}

    def inner(*args, **kwargs) -> Any:
        cache_key = args + tuple(kwargs.items())
        if cache_key not in result:
            print("Calculating new result")
            result[cache_key] = func(*args, **kwargs)
        else:
            print("Getting from cache")
        return result[cache_key]
    return inner
