from typing import Any, Callable


def cache(func: Callable) -> Callable:
    cache_box = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        key = (args, frozenset(kwargs.items()))
        if key in cache_box:
            print("Getting from cache")
            return cache_box[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            cache_box[key] = result
            return result

    return wrapper
