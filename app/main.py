from typing import Callable, Any
import functools


def cache(func: Callable) -> Callable:
    cached_result = {}

    @functools.wraps(func)
    def inner(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))

        if key in cached_result:
            print("Getting from cache")
            return cached_result[key]

        print("Calculating new result")
        result = func(*args, **kwargs)
        cached_result[key] = result

        return result
    return inner
