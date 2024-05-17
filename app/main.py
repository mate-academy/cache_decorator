from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_ = {}

    def inner(*args) -> Any:
        key = args
        if key in cache_:
            print("Getting from cache")
            return cache_[key]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_[key] = result
            return result
    return inner
