from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cache_ = {}

    def inner(*args: tuple) -> Any:
        if args in cache_:
            print("Getting from cache")
            result = cache_[args]
        else:
            print("Calculating new result")
            result = func(*args)
            cache_[args] = result
        return result
    return inner
